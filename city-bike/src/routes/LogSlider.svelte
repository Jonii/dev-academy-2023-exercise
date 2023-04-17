<script lang="ts">
    let sliderValue = 100;
    let selectedTime = 0;
    let selectedTimeFinal = 0;
    let centerValue = 100;
    let min = 0;
    let max = 200;

    export let selectedDate: Date = new Date();
    let dateSelectorDisplayVal = new Date();
    const timeRadius = 1000 * 60 * 60 * 12;

    
    function updateSelectedTimeBasedOn(baseTime: Date = selectedDate) {
        const relativeValue = (sliderValue - centerValue) / (max - min);
        const timeChange =
            timeRadius * Math.pow(relativeValue, 2) * Math.sign(relativeValue);
            selectedTime = timeChange;
            const newDate = new Date();
        newDate.setTime(baseTime.getTime() + selectedTime);
        dateSelectorDisplayVal = newDate;
    }
    function updateSelectedTime() {
        updateSelectedTimeBasedOn(selectedDate);
    }
    $: updateSelectedTimeBasedOn(selectedDate);
    
    function resetSlider() {
        setTimeout(() => {
            selectedDate.setTime(selectedDate.getTime() + selectedTime);
            selectedTimeFinal = selectedTime;
            sliderValue = centerValue;
        }, 100);
    }
    //$: console.log("Selected time:", selectedTime);
</script>

<div>
    <input
        type="range"
        bind:value={sliderValue}
        {min}
        {max}
        on:input={updateSelectedTime}
        on:mouseup={resetSlider}
    />
    <p>Slider value: {sliderValue}</p>
    <!---

    <p>Selected time: {selectedTime} ms</p>
    <p>
        Selected time: <span>{selectedDate.toLocaleTimeString()}</span>
        <span style="font-size: 0.8rem"
            >{selectedDate.toLocaleDateString("fi-Fi")}</span
        >
    </p>
    -->
    <p>
        Selected time: <span>{dateSelectorDisplayVal.toLocaleTimeString()}</span>
        <span style="font-size: 0.8rem">{dateSelectorDisplayVal.toLocaleDateString("fi-Fi")}</span>
    </p>
</div>
