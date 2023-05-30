<script lang="ts">
    import { onMount } from 'svelte';
    import type { StationDataSchema } from '../../types.js';
    import StationBadge from '../../StationBadge.svelte';

    export let data;
    const stationId = data.stationId;

    let stationData: StationDataSchema;

    function getStationData() {
        fetch(`http://localhost:8000/api/stations/by_id/${stationId}`)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                stationData = data;
            });
    }
    onMount(() => {
        getStationData();
    });
</script>
<h1>
    <StationBadge { stationData } />
</h1>