<script lang="ts">
    import { onMount } from 'svelte';
    import { selectedDate } from './stores';

    let dateInput: string;

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

    $: {
        console.log(dateInput);
        if (dateInput !== formatDate($selectedDate)) {
            dateInput = formatDate($selectedDate);
        }
    }
</script>

<input type="date" bind:value={dateInput} on:change={handleDateChange}>