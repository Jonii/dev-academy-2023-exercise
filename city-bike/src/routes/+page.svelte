<script lang="ts">
    import { onMount } from 'svelte';
    import type { BikeTrip, BikeTripRaw } from './types';
    import Table from './Table.svelte';
    import { selectedDate } from './stores';
    import DatePicker from './DatePicker.svelte';
    import CsvUploader from './CsvUploader.svelte';

    const baseUrl = `http://localhost:8000/api/`;

    let isMounted = false;
    let firstFetch = true;

    let data: BikeTrip[] = [];
    const minInMillis = 1000 * 60;
    
    async function fetchData(time: Date) {
        console.log("fetching data");
        const fetch_url = fetchDataForDateInterval(time, new Date(time.getTime() + minInMillis));
        const response = await fetch(fetch_url);
        console.log(response.status);
        const rawData: BikeTripRaw = await response.json();
        console.log(JSON.stringify(rawData.trips[0]));
        data = rawData.trips.map(item => ({
            ...item,
            Return: new Date(item.Return),
            Departure: new Date(item.Departure),
        }));
        if (firstFetch) {
            firstFetch = false;
            $selectedDate = new Date(rawData.start_time);
        }
        console.log($selectedDate);
    }

    function shouldFetch(): boolean {
        return isMounted;
    }

    function getStartTime(): Date {
        return new Date(2021, 4, 1, 0, 0, 0);
    }

    function formatDate(date: Date): string {
        return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}T${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
    }
    
    function fetchDataForDateInterval(start_time: Date, end_time: Date) {
        start_time = new Date(start_time.getTime())
        start_time.setMilliseconds(0);
        end_time = new Date(end_time.getTime());
        end_time.setMilliseconds(0);
        
        const bikeApiURL = baseUrl + 'bike-trips?';

        const startTimeQuery = `start_time=${formatDate(start_time)}`;
        const endTimeQuery = `end_time=${formatDate(end_time)}`;
        return bikeApiURL + startTimeQuery + '&' + endTimeQuery;
    }

    onMount(() => {
        isMounted = true;
        const startTime = getStartTime();
        fetchData(startTime);
        $selectedDate = startTime;
    });
    $: shouldFetch() && fetchData($selectedDate);
</script>

<div class="page-content">
    <p>Here we have bike stuff</p>

    <CsvUploader />
  
    <br>
  
    <DatePicker />
    
    <br>

    <Table data={data}/>
</div>

<style>
    .page-content {
        text-align: center;
        margin: auto;
    }
</style>