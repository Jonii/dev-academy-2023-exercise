<script lang="ts">
    import type { stationDataSchema } from "./types";

    export let stationData: stationDataSchema | undefined = undefined;
    export const size: number = 1;
</script>

{#if stationData}
<a href={`/stations/${stationData?.ID}`}>
    <div class="station-badge">
        <div class="name">
            {stationData.Nimi}
        </div>
        <div class="grid-container">
            <div class="id">
                ID: {stationData.ID}
            </div>
            <div class="city">
                City: {stationData.Kaupunki}
            </div>
            <div class="address">
                {stationData.Osoite}
            </div>
        </div>
    </div>
</a>
{:else}
Station not found
{/if}

<style>
    .station-badge {
        display: inline-block;
        padding: 0.4em 0.7em;
        margin: 0.3em;
        border: 1px solid #aaa;
        border-radius: 5px;
        background-color: #f8f8f8;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        font-family: Arial, sans-serif;
        font-size: 1rem;
        color: #333;
    }
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr; 
        grid-template-rows: auto;
        gap: 0.3em; 
    }
    
    .station-badge .name {
        font-weight: bold;
    }
    
    .station-badge .id, .station-badge .city, .operator, .address {
        font-size: 0.6em;
        color: #777;
    }
    .operator, .address {
        grid-column: 1 / 3;
    }
    </style>
    