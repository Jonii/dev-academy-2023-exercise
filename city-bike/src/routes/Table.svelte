<script lang="ts">
    import type { BikeTrip } from './types';
    
    export let data: BikeTrip[] = [];
    function formatDate(date: Date) {
        return date.toLocaleDateString() + " " + date.toLocaleTimeString("fi-Fi", {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
        });
    }
    function formatTripDuration(duration: number) {
        const seconds = duration % 60;
        const minutes = Math.floor(duration / 60) % 60;
        const hours = Math.floor(duration / 3600);
        if (hours === 0) {
            return minutes + "m " + String(seconds).padStart(2, '0') + "s";
        }
        return hours + "h " + String(minutes).padStart(2, '0') + "m " + String(seconds).padStart(2, '0') + "s";
    }

</script>

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

<style>
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