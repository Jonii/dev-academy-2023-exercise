<script lang="ts">
    import { onMount } from 'svelte';
    import type { DailyStats, StationDataSchema } from '../../types.js';
    import StationBadge from '../../StationBadge.svelte';
    import { each } from 'svelte/internal';

    export let data;
    const stationId = data.stationId;

    let stats: Map<string, DailyStats[]>;
    let daily_stats: {date: string, items: DailyStats[]}[] = [];
    let stationData: StationDataSchema;

    function getStationData() {
        fetch(`http://localhost:8000/api/stations/by_id/${stationId}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                stationData = data;
            });
    }
    function getStationStats() {
        fetch(`http://localhost:8000/api/daily_stats?departure_station_id=${stationId}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                const stats_raw: DailyStats[] = data;
                let grouped = stats_raw.reduce((groupedStats: { [key: string]: DailyStats[] }, stat) => {
                    (groupedStats[stat['date']] = groupedStats[stat['date']] || []).push(stat);
                    return groupedStats;
                }, {});
                daily_stats = Object.keys(grouped).sort().map(date => ({date, items: grouped[date]}));
            });
    }

    onMount(() => {
        getStationData();
        getStationStats();
    });
</script>
<h1>
    <StationBadge { stationData } />
    {#each daily_stats as day}
        <h6>{day.date}</h6>
        <ul>
            {#each day.items as stat}
                <li>
                    {stat['Return station name']}: {stat['Count']}
                </li>
            {/each}
        </ul>
    {/each}
</h1>

<style>
    ul {
        list-style-type: none;
        font-size: 0.8rem;
    }
</style>