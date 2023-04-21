<script lang="ts">
    let centerValue = 50;
    let sliderValue = centerValue;
    let min = 0;
    let max = 100;
    export let valueToUnit = _valueToUnit;
    export let selectedValue: Date = new Date();
    let dateSelectorDisplayVal = new Date();
    const timeRadius = 1000 * 60 * 60 * 12;

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
    />
    <p>Slider value: {sliderValue}</p>

    <p>
        Selected time: <span>{dateSelectorDisplayVal.toLocaleTimeString()}</span>
        <span style="font-size: 0.8rem">{dateSelectorDisplayVal.toLocaleDateString("fi-Fi")}</span>
    </p>
</div>
