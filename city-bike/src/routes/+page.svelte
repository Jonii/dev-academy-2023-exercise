<script lang="ts">
    import { onMount } from 'svelte';
    type BikeTrip = {
        Departure: Date;
        Return: Date;
        "Departure station id": number;
        "Departure station name": string;
        "Return station id": number;
        "Return station name": string;
        "Covered distance (m)": number;
        "Duration (sec.)": number;
    };
    type BikeTripRaw = {
        Departure: string;
        Return: string;
        "Departure station id": number;
        "Departure station name": string;
        "Return station id": number;
        "Return station name": string;
        "Covered distance (m)": number;
        "Duration (sec.)": number;
    }
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
    function formatDate(date: Date) {
        return date.toLocaleDateString() + " " + date.toLocaleTimeString("fi-Fi", {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit"
        });
    }
    function formatTripDuration(duration: number) {
        const seconds = duration % 60;
        const minutes = Math.floor(duration / 60) % 60;
        const hours = Math.floor(duration / 3600);
        if (hours === 0) {
            return minutes + ":" + String(seconds).padStart(2, '0');
        }
        return hours + ":" + String(minutes).padStart(2, '0') + ":" + String(seconds).padStart(2, '0');
    }
    onMount(() => { 
        fetchData();
    });
</script>

<div class="page-content">
    <p>Here we have bike stuff</p>
    
    <div class="table">
        <div class="tableheader">
            <div class="tablecell">Departure</div>
            <div class="tablecell">Return time</div>
            <div class="tablecell">Trip duration</div>
            <div class="tablecell">Departure station</div>
            <div class="tablecell">Return station</div>
            <div class="tablecell">Covered distance</div>
        </div>
        {#each data as datum}
            <div class="tablerow">
                <div class="tablecell">{formatDate(datum["Departure"])}</div>
                <div class="tablecell">{formatDate(datum["Return"])}</div>
                <div class="tablecell">{formatTripDuration(datum["Duration (sec.)"])}</div>
                <div class="tablecell">{datum["Departure station name"]}<br>{datum["Departure station id"]}</div>
                <div class="tablecell">{datum["Return station name"]}<br>{datum["Return station id"]}</div>
                <div class="tablecell">{datum["Covered distance (m)"]/1000} km</div>
            </div>
        {/each}
    </div>
</div>

<style>
    .page-content {
        text-align: center;
        margin: auto;
    }
    .table {
        margin: auto;
        display: table;
        border: 1px solid #ccc;
        border-collapse: collapse;
    }
    .tablerow {
        display: table-row;
    }
    .tablecell {
        display: table-cell;
        padding: 8px;
        border: 1px solid #ccc;
        text-align: center;
    }
    .tableheader > .tablecell {
        font-weight: 500;
        color: #a86;
        border-bottom: 1px solid #555;
    }
    .tableheader {
        display: table-header-group;
    }
</style>