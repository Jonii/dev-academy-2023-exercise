<script lang="ts">
    import { flip } from 'svelte/animate';
    import { fly } from 'svelte/transition';
    import { tweened } from 'svelte/motion';
    import { linear } from 'svelte/easing';
    import { createEventDispatcher } from 'svelte';
    import { selectedDate } from './stores';

    const dispatch = createEventDispatcher();

    const animationDuration = 150;
    const min = 0;
    const max = 1001;
    const centerValue = (min + max) / 2;
    
    let sliderValue = centerValue;

    let sliderElement: HTMLElement;
    let dateSelectorDisplayVal = new Date();
    const timeRadius = 1000 * 60 * 60 * 6;
    let markers: Marker[] = generateNonLinearMarkers(10, $selectedDate, centerValue);

    $: sliderElement && sliderElement.style.setProperty('--highlight-center', `${sliderValue * 100 / (max - min)}%`);
    $: console.log(selectedDate);
    //$: console.log(centerValue);
    //$: console.log(sliderValue);
    //$: tweenDuration = animateThumb ? animationDuration : 200;


    function valueToUnit(basevalue: Date, rawUnitless: number): Date {
        timeRadius;
        const scaledUnitless =
            timeRadius * valueToUnitlessScaled(rawUnitless) + 100;
        const newDate = new Date();
        newDate.setTime(basevalue.getTime() + scaledUnitless);
        return newDate;
    }

    function valueToUnitlessScaled(sliderVal: number) {
        const normalized = normalizedSliderValue(sliderVal);
        return Math.pow(normalized, 3);
    }

    function normalizedSliderValue(val: number): number {
        return (val - centerValue) / ((max - min) / 2);
    }

    function markerWidth(pos: number, baseScale: number = 60) {
        const val = Math.pow(Math.abs(normalizedSliderValue(pos)) + 1, -3) * baseScale;
        return val;
    }    

    function unitToValue(time: number, selectedValue: Date, centerValue: number) {
        const delta = (time - selectedValue.getTime()) / timeRadius;
        const deltaUnscaled = delta > 0 ? Math.pow(delta, 1/3) : -Math.pow(-delta, 1/3);
        return centerValue + (deltaUnscaled * ((max - min) / 2));
    }

    function updateViewValue(baseTime: Date = $selectedDate) {
        const newDate: Date = valueToUnit(baseTime, sliderValue);
        dateSelectorDisplayVal = newDate;
    }
    $: updateViewValue($selectedDate);
    
    async function sliderSelectTime() {
        console.log("Resetting slider");
        markers = generateNonLinearMarkers(10, dateSelectorDisplayVal, centerValue);
        
        $selectedDate.setTime(dateSelectorDisplayVal.getTime());
        $selectedDate = $selectedDate;
        
        const tweenedValue = tweened(sliderValue, { duration: animationDuration, easing: linear });
        tweenedValue.subscribe(($value) => {
            sliderValue = $value;
        });

        await tweenedValue.set(centerValue);

        sliderValue = centerValue;
        
        dispatch("dateSet", {
            date: selectedDate
        });

    }

    function setSlider(value: Date) {
        console.log("Setting slider value to " + value.toLocaleTimeString() + ".");
        markers = generateNonLinearMarkers(10, value, centerValue);
        sliderValue = centerValue;
        dateSelectorDisplayVal = value;
    }

    $: setSlider($selectedDate);
    $: console.log($selectedDate);

    type Marker = {
        position: number;
        date: Date;
        dateKey: number;
        isVisible: boolean;
        markerWidth: number;
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
            markerPositions.push({position: position, date: new Date(t), dateKey: t, isVisible: isVisible, markerWidth: markerWidth(position)});
        }
        //console.log(JSON.stringify(markerPositions));
        return markerPositions;
    }

    function boxAdjustingTerm(marker: Marker): number {
        return (marker.markerWidth * 0.155 * (marker.position - centerValue) / (max-min))
    }

    $: sliderElement && sliderElement.style.setProperty('--thumb-width', `${Math.round(markerWidth(sliderValue, 100))}px`);
</script>

<div>
    <div class="slider-container">
        <input
        type="range"
        bind:value={sliderValue}
        {min}
        {max}
        on:input={() => updateViewValue($selectedDate)}
        on:change={sliderSelectTime}
        bind:this={sliderElement}
        />
        {#each markers as marker (marker.dateKey)}
            <div 
                class="slider-marker" 
                style="left: {marker.position * 100 / (max - min) - boxAdjustingTerm(marker)}%; width: {marker.markerWidth}px"
                animate:flip={{ duration: animationDuration }}
                transition:fly="{{ x: Math.sign(marker.position - centerValue) * 150, duration: animationDuration }}"
            >{marker.date.getHours()}:00</div>
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
        --thumb-transform: none;
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
        transform: var(--thumb-transform);
    }

    input[type=range]::-moz-range-thumb {
        width: var(--thumb-width);
        height: var(--thumb-height);
        transform: var(--thumb-transform);
    }

    input[type=range]::-ms-thumb {
        width: var(--thumb-width);
        height: var(--thumb-height);
        transform: var(--thumb-transform);
    }

    input[type=range]::-webkit-slider-runnable-track {
        background: #367ebd;
    }

    input[type=range]::-moz-range-track {
        width: calc(100% - 6px);
        height: 15px;
        box-sizing: border-box;
        cursor: pointer;
        background: radial-gradient(circle at var(--highlight-center), #fadfac 20%, #0be930 100%);
                    /* 
                    linear-gradient(to right, transparent 0% calc(var(--highlight-true-center) - 1%), #033112 calc(var(--highlight-true-center) - 1%) calc(var(--highlight-true-center) + 1%), transparent calc(var(--highlight-true-center) + 1%)),
                    */        
        border: 2px outset black;
    }

    input[type=range]::-ms-track { 
        border-color: transparent;
        color: transparent;
    }
    .slider-container {
        position: relative;
        overflow: hidden;
        margin: 10%;
        
    }
    .slider-marker {
        position: absolute;
        box-sizing: border-box;
        width: 2px;
        height: 16px;
        background: #857cff;
        border-radius: 5px;
        border: 1px solid black;
        bottom: -1px;
        transform: translateX(-50%);
        font-size: 10px;
        overflow: hidden;
    }
</style>
