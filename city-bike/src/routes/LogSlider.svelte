<script lang="ts">
    const trueCenter = 50;
    let centerValue = trueCenter;
    let sliderValue = centerValue;
    let min = 0;
    let max = 100;
    export let valueToUnit = _valueToUnit;
    export let selectedValue: Date = new Date();
    let sliderElement: HTMLElement;
    let dateSelectorDisplayVal = new Date();
    const timeRadius = 1000 * 60 * 60 * 12;

    $: sliderElement && sliderElement.style.setProperty('--highlight-center', `${sliderValue}%`);
    $: sliderElement && console.log(sliderElement.style.getPropertyValue("--highlight-center"));

    function _valueToUnit(basevalue: Date, rawUnitless: number): Date {
        timeRadius;        
        const scaledUnitless =
            timeRadius * Math.pow(rawUnitless, 2) * Math.sign(rawUnitless);
        const newDate = new Date();
        newDate.setTime(basevalue.getTime() + scaledUnitless);
        return newDate;
    }

    function normalizedSliderValue(): number {
        if (sliderValue > centerValue) {
            return (sliderValue - centerValue) / (max - centerValue);
        }
        return (sliderValue - centerValue) / (centerValue - min);
    }

    function updateViewValue(baseTime: Date = selectedValue) {
        const newDate: Date = valueToUnit(baseTime, normalizedSliderValue());
        dateSelectorDisplayVal = newDate;
    }
    $: updateViewValue(selectedValue);
    
    function resetSlider() {
        selectedValue.setTime(dateSelectorDisplayVal.getTime());
        centerValue = Math.round((sliderValue * 2 + centerValue) / 3);
        
        sliderValue = centerValue;
    }
</script>

<div>
    <input
        type="range"
        bind:value={sliderValue}
        {min}
        {max}
        on:input={() => updateViewValue(selectedValue)}
        on:change={resetSlider}
        bind:this={sliderElement}
    />
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
        --thumb-height: 35px;
        --thumb-width: 40px;
        --highlight-center: 50%;
    }

    input[type=range] {
        -webkit-appearance: none;
        height: 35px; 
        padding: 0;	
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
        height: 5px;
        cursor: pointer;
        background: radial-gradient(circle at var(--highlight-center), #fadfac 20%, #0be930 100%);
        border: 1px outset black;
    }

    input[type=range]::-ms-track { 
        border-color: transparent;
        color: transparent;
    }
</style>
