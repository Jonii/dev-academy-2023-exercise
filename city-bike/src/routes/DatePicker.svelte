<script lang="ts">
    import { onMount } from 'svelte';
    import { selectedDate } from './stores';

    let dateInput: string;
    let timeInput: string;


    function formatDate(date: Date): string {
        const yearString = date.getFullYear();
        const monthString = (date.getMonth() + 1).toString().padStart(2, '0');
        const dateString = date.getDate().toString().padStart(2, '0');
        return yearString + '-' + monthString + '-' + dateString;
    }

    onMount(() => {
        dateInput = formatDate($selectedDate);
    });

    function handleDateChange() {
        console.log(dateInput);
        const date = new Date(dateInput);
        date.setHours($selectedDate.getHours(), $selectedDate.getMinutes(), $selectedDate.getSeconds());
        $selectedDate = date;
    }

    function handleTimeChange() {
        console.log(timeInput);
        const time = new Date($selectedDate);
        const [hours, minutes] = timeInput.split(':').map(item => parseInt(item));
        time.setHours(hours, minutes, 0);
        $selectedDate = time;
    }

    function addDays(date: Date, days: number): Date {
        const result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
    }
    function addMinutes(date: Date, minutes: number): Date {
        const result = new Date(date);
        result.setMinutes(result.getMinutes() + minutes);
        return result;
    }

    $: {
        console.log(dateInput);
        if (dateInput !== formatDate($selectedDate)) {
            dateInput = formatDate($selectedDate);
        }
    }

    $: {
        console.log(timeInput);
        if (timeInput !== $selectedDate.toTimeString()) {
            timeInput = $selectedDate.toTimeString().split(' ')[0].split(':').slice(0, 2).join(':');
        }
    }
</script>
<div class="container">
    <div>
        <div>
            {$selectedDate.toLocaleDateString(undefined, {weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'})}
        </div>
        <div>
            <button on:click={() => $selectedDate = addDays($selectedDate, -1)}>&lt;</button>
            <input type="date" bind:value={dateInput} on:change={handleDateChange}>
            <button on:click={() => $selectedDate = addDays($selectedDate, 1)}>&gt;</button>
        </div>
    </div>
    <div>
        <div style="height:1em">
        </div>
        <div>
            <button on:click={() => $selectedDate = addMinutes($selectedDate, -15)}>&lt;&lt;</button>
            <button on:click={() => $selectedDate = addMinutes($selectedDate, -1)}>&lt;</button>
            <input type="time" bind:value={timeInput} on:change={handleTimeChange}>
            <button on:click={() => $selectedDate = addMinutes($selectedDate, 1)}>&gt;</button>
            <button on:click={() => $selectedDate = addMinutes($selectedDate, 15)}>&gt;&gt;</button>
        </div>
    </div>
</div>

<style>
    .container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }
    .container > div {
        margin: 0.5rem 3rem;
    }
</style>