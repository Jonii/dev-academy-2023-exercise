<script lang="ts">
    import { onMount } from 'svelte';
    type BikeTrip = {
        Departure: String;
        "Departure station name": String;
    };
    let data: BikeTrip[] = [];
    async function fetchData() {
        const response = await fetch("http://localhost:8000/api/bike-trips");
        console.log(response.status);
        data = await response.json();
    }
    onMount(() => { 
        fetchData();
    });
</script>

<div class="page-content">
    <p>Here we have bike stuff</p>
    
    <div class="table">
        <div class="tableheader">
            <div class="tablecell">Greetings</div>
            <div class="tablecell">For you</div>
        </div>
        <div class="tablerow">
            <div class="tablecell">Hello</div>
            <div class="tablecell">There</div>
        </div>
        {#each data as datum}
            <div class="tablerow">
                <div class="tablecell">{datum["Departure"]}</div>
                <div class="tablecell">{datum["Departure station name"]}</div>
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