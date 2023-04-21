<script lang="ts">
    import { flip } from 'svelte/animate';
    import { fly } from 'svelte/transition';

    const trueCenter = 50;
    let centerValue = trueCenter;
    let sliderValue = centerValue;
    let min = 0;
    let max = 100;
    export let valueToUnit = _valueToUnit;
    export let selectedValue: Date = new Date();
    let sliderElement: HTMLElement;
    let dateSelectorDisplayVal = new Date();
    const timeRadius = 1000 * 60 * 60 * 6;
    let markers: Marker[] = generateNonLinearMarkers(50, selectedValue, centerValue);

    $: sliderElement && sliderElement.style.setProperty('--highlight-center', `${sliderValue}%`);
    $: console.log(centerValue);
    $: console.log(sliderValue);
    function _valueToUnit(basevalue: Date, rawUnitless: number): Date {
        timeRadius;        
        const scaledUnitless =
            timeRadius * Math.pow(rawUnitless, 3); //* Math.sign(rawUnitless);
        const newDate = new Date();
        newDate.setTime(basevalue.getTime() + scaledUnitless);
        return newDate;
    }

    function normalizedSliderValue(): number {
        return (sliderValue - centerValue) / ((max - min) / 2);
    }

    function updateViewValue(baseTime: Date = selectedValue) {
        const newDate: Date = valueToUnit(baseTime, normalizedSliderValue());
        dateSelectorDisplayVal = newDate;
    }
    $: updateViewValue(selectedValue);
    
    function resetSlider() {
        console.log("Resetting slider and doing all such stuff");
        selectedValue.setTime(dateSelectorDisplayVal.getTime());
        centerValue = Math.round((sliderValue + trueCenter * 3) / 4);
        sliderValue = centerValue;
        markers = generateNonLinearMarkers(50, selectedValue, centerValue);
    }

    function unitToValue(time: number, selectedValue: Date, centerValue: number) {
        const delta = (time - selectedValue.getTime()) / timeRadius;
        const deltaUnscaled = delta > 0 ? Math.pow(delta, 1/3) : -Math.pow(-delta, 1/3);
        return centerValue + (deltaUnscaled * 50);
    }
    type Marker = {
        position: number;
        date: Date;
        dateKey: number;
        isVisible: boolean;
    }
    function generateNonLinearMarkers(markerCount: number, selectedValue: Date, centerValue: number): Marker[] {
        const markerPositions = [];
        const closestHour = new Date(selectedValue.getTime());
        closestHour.setMinutes(0);
        closestHour.setSeconds(0);
        closestHour.setMilliseconds(0);
        const hour = 1000 * 60 * 60;
        for (let i = -1 * markerCount; i <= markerCount; i++) {
            const t = closestHour.getTime() - (i * hour);
            const position = unitToValue(t, selectedValue, centerValue);
            const isVisible = (position >= min && position <= max);
            if (!isVisible) {
                continue;
            }
            markerPositions.push({position: position, date: new Date(t), dateKey: t, isVisible: isVisible});
        }
        console.log(JSON.stringify(markerPositions));
        return markerPositions;
    }
</script>

<div>
    <div class="slider-container">
        <input
        type="range"
        bind:value={sliderValue}
        {min}
        {max}
        on:input={() => updateViewValue(selectedValue)}
        on:change={resetSlider}
        bind:this={sliderElement}
        />
        {#each markers as marker (marker.dateKey)}
            <div 
                class="slider-marker" 
                style="left: {marker.position}%"
                animate:flip={{ duration: 100 }}
                transition:fly="{{ x: Math.sign(marker.position - 50) * 150, duration: 100 }}"
            ></div>
        {/each}
    </div>
    <!--
        <p>Slider value: {sliderValue}</p>
    -->

    <p>
        Selected time: <span>{dateSelectorDisplayVal.toLocaleTimeString()}</span>
        <span style="font-size: 0.8rem">{dateSelectorDisplayVal.toLocaleDateString("fi-Fi")}</span>
    </p>
</div>

<style>
    :root {
        --thumb-height: 15px;
        --thumb-width: 40px;
        --highlight-center: 50%;
        --highlight-true-center: 50%;
    }

    input[type=range] {
        -webkit-appearance: none;
        height: 35px; 
        padding: 0;
        width: 100%;
    }

    input[type=range]::-webkit-slider-thumb {
        -webkit-appearance: none;
        box-sizing: content-box;
        width: var(--thumb-width);
        height: var(--thumb-height);
    }

    input[type=range]::-moz-range-thumb {
        width: var(--thumb-width);
        height: var(--thumb-height);
    }

    input[type=range]::-ms-thumb {
        width: var(--thumb-width);
        height: var(--thumb-height);
    }

    input[type=range]::-webkit-slider-runnable-track {
        background: #367ebd;
    }

    input[type=range]::-moz-range-track {
        width: 100%;
        height: 15px;
        cursor: pointer;
        background: radial-gradient(circle at var(--highlight-center), #fadfac 20%, #0be930 100%);
                    /* 
                    linear-gradient(to right, transparent 0% calc(var(--highlight-true-center) - 1%), #033112 calc(var(--highlight-true-center) - 1%) calc(var(--highlight-true-center) + 1%), transparent calc(var(--highlight-true-center) + 1%)),
                    */        
        border: 1px outset black;
    }

    input[type=range]::-ms-track { 
        border-color: transparent;
        color: transparent;
    }
    .slider-container {
        position: relative;
    }
    .slider-marker {
        position: absolute;
        width: 2px;
        height: 10px;
        background: #000000;
        bottom: 5px;
    }
</style>
