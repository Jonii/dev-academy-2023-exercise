<script lang="ts">
    import { onMount } from 'svelte';
    import type { BikeTrip, BikeTripRaw } from './types';
    import Table from './Table.svelte';

    let data: BikeTrip[] = [];
    async function fetchData() {
        const response = await fetch("http://localhost:8000/api/bike-trips");
        console.log(response.status);
        const rawData: BikeTripRaw[] = await response.json();
        data = rawData.map(item => ({
            ...item,
            Return: new Date(item.Return),
            Departure: new Date(item.Departure),
        }));
    }

    onMount(() => { 
        fetchData();
    });
</script>

<div class="page-content">
    <p>Here we have bike stuff</p>
    
    <Table data={data}/>
</div>

<style>
    .page-content {
        text-align: center;
        margin: auto;
    }
</style>