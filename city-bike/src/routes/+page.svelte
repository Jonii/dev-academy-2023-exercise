<script lang="ts">
    import { onMount } from 'svelte';
    import type { BikeTrip, BikeTripRaw } from './types';
    import Table from './Table.svelte';
    import LogSlider from './LogSlider.svelte';

    let data: BikeTrip[] = [];
    let start_time = new Date();
    async function fetchData() {
        const response = await fetch("http://localhost:8000/api/bike-trips");
        console.log(response.status);
        const rawData: BikeTripRaw = await response.json();
        data = rawData.trips.map(item => ({
            ...item,
            Return: new Date(item.Return),
            Departure: new Date(item.Departure),
        }));
        start_time = new Date(rawData.start_time);
    }

    onMount(() => { 
        fetchData();
    });
</script>

<div class="page-content">
    <p>Here we have bike stuff</p>
    <LogSlider bind:selectedDate={start_time}/>
    
    <Table data={data}/>
</div>

<style>
    .page-content {
        text-align: center;
        margin: auto;
    }
</style>