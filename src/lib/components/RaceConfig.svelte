<script lang="ts">
  import type { RaceConfigType } from '$lib/types'
  export let items: string[]
  export let raceConfig: RaceConfigType = {
    votesToWin: 10,
    autoStep: 0
  };

  // Function to handle input changes and enforce constraints
  function handleInput(prop: keyof RaceConfigType, event: Event) {
    const input = event.target as HTMLInputElement;
    const numValue = Math.max(0, parseInt(input.value, 10));
    if (prop === 'votesToWin') {
      raceConfig.votesToWin = Math.min(numValue, 9999); // Max 9999
      if (raceConfig.votesToWin === 0) {
        raceConfig.votesToWin = 1
      }
    } else if (prop === 'autoStep') {
      raceConfig.autoStep = numValue; // Non-negative
    }
  }

  $: raceConfig.votesToWin = Math.min(
    Math.max(1, raceConfig.votesToWin),
    9999
  )

</script>
<style>
  .form-container {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .form-label {
    display: flex;
  }

  label {
    padding-left: 14px;
  }

  .input-container {
    width: 5.5rem;
  }

  input[type="number"] {
    padding: 4px;
    text-align: center;
    border: 1px solid #ccc;
    border-radius: 5px;
  }

  label {
    margin-top: 5px;
    text-align: left;
  }

  .checkbox-item {
    display: flex;
    align-items: center;
  }

  /* Toggle Switch */
  .checkbox-item input[type="checkbox"] {
    appearance: none;
    width: 40px;
    height: 20px;
    background: #777;
    border-radius: 10px;
    position: relative;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  .checkbox-item input[type="checkbox"]:checked {
    background: var(--color-link-text);
  }

  .checkbox-item input[type="checkbox"]::before {
    content: "";
    position: absolute;
    width: 16px;
    height: 16px;
    background: white;
    border-radius: 50%;
    top: 2px;
    left: 2px;
    transition: transform 0.3s ease;
  }

  .options-container {
    padding-bottom: 2rem;
  }

  .checkbox-item input[type="checkbox"]:checked::before {
    transform: translateX(20px);
  }

</style>
<div class="options-container">
  <div class="row justify-between full-width">
    <h2>Options</h2>
  </div>
  <form class="form-container">
    <div class:hidden={items.length < 1} class="checkbox-item">
      <div class="input-container">
        <input type="checkbox" bind:checked={raceConfig.linkToRottenTomatoes} name="link-to-rt">
      </div>
      <label  for="link-to-rt">
        Link options to RottenTomatoes
      </label>
    </div>
    <div class="form-label">
      <div class="input-container">
        <input
          id="votesToWin"
          type="number"
          min="1"
          max="9999"
          step="1"
          bind:value={raceConfig.votesToWin}
          on:input={event => handleInput('votesToWin', event)}
        >
        </div>
        <label for="votesToWin">
          Votes to win
        </label>
      </div>
      <div class="form-label">
        <div class="input-container">
          <input
            id="autoStep"
            type="number"
            min="0"
            max="9999"
            step="1"
            bind:value={raceConfig.autoStep}
            on:input={event => handleInput('autoStep', event)}
          >
          </div>
          <label for="autoStep">
            Auto step every N seconds
            <br>(0 for manual step)
          </label>
        </div>
      </form>
    </div>

