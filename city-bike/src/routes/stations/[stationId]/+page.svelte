<script lang="ts">
    import { onMount } from 'svelte';
    import type { stationDataSchema } from './types.js';
    import Station from '../../Station.svelte';

    export let data;
    const stationId = data.stationId;

    let stationData: stationDataSchema;

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
    <Station { stationData } />
</h1>