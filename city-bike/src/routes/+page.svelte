<script lang="ts">
    import { onMount } from 'svelte';
    import type { BikeTrip, BikeTripRaw } from './types';
    import Table from './Table.svelte';
    import LogSlider from './LogSlider.svelte';
    import { selectedDate } from './stores';

    let isMounted = false;
    let muteFetch = false;

    let data: BikeTrip[] = [];
    const minInMillis = 1000 * 60;
    async function fetchData(time: Date | undefined = undefined) {
        const fetch_url = fetchUrl(time, time ? new Date(time.getTime() + minInMillis) : undefined);
        const response = await fetch(fetch_url);
        console.log(response.status);
        const rawData: BikeTripRaw = await response.json();
        data = rawData.trips.map(item => ({
            ...item,
            Return: new Date(item.Return),
            Departure: new Date(item.Departure),
        }));
        if ($selectedDate.toISOString() !== rawData.start_time) {
            muteFetch = true;
            $selectedDate = new Date(rawData.start_time);
        }
        console.log($selectedDate);
    }
    
    function shouldFetch(): boolean {
        const fetchIsMuted = !muteFetch;
        muteFetch = false;
        return isMounted && fetchIsMuted;
    }
    
    function fetchUrl(start_time: Date | undefined = undefined, end_time: Date | undefined = undefined) {
        const baseUrl = `http://localhost:8000/api/bike-trips?`;
        const startTimeQuery = start_time ? `start_time=${start_time.toISOString()}` : '';
        const endTimeQuery = end_time ? `end_time=${end_time.toISOString()}` : '';
        if (startTimeQuery && endTimeQuery) {
            return baseUrl + startTimeQuery + '&' + endTimeQuery;
        } else if (startTimeQuery) {
            return baseUrl + startTimeQuery;
        } else if (endTimeQuery) {
            return baseUrl + endTimeQuery;
        } else {
            return baseUrl;
        }
    }

    onMount(() => {
        isMounted = true;
        fetchData();
    });
    $: shouldFetch() && fetchData($selectedDate);
    
</script>

<div class="page-content">
    <p>Here we have bike stuff</p>
    <LogSlider />
    
    <Table data={data}/>
</div>

<style>
    .page-content {
        text-align: center;
        margin: auto;
    }
</style>