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
        const [hours, minutes, seconds] = timeInput.split(':').map(item => parseInt(item));
        time.setHours(hours, minutes, seconds);
        $selectedDate = time;
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
            timeInput = $selectedDate.toTimeString().split(' ')[0];
        }
    }
</script>

<input type="date" bind:value={dateInput} on:change={handleDateChange}>
<input type="time" step="1" bind:value={timeInput} on:change={handleTimeChange}>