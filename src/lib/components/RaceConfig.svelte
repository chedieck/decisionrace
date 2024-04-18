<script lang="ts">
  import type { RaceConfigType } from '$lib/types'
  export let raceConfig: RaceConfigType = {
    votesToWin: 5,
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
  .form-label {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 20px; /* Space between label-input pairs */
  }

  label {
    font-weight: bold;
    margin-bottom: 5px; /* Space between the label text and the input */
  }

  input {
    width: 100%; /* Make input take full width of its container */
    padding: 8px; /* Padding inside the input for better readability */
    box-sizing: border-box; /* Include padding and border in the width */
  }

  .form-container {
    display: flex;
    flex-direction: column; /* Stack the label-input pairs vertically */
    align-items: flex-start; /* Align items to the start of the flex container */
    padding: 20px; /* Padding around the entire form */
    max-width: 400px; /* Maximum width of the form */
    margin: auto; /* Center the form horizontally on the page */
  }
  @media (max-width: 768px) {
    input {
      width: 34%;
    }
    label {
      width: 66%;
    }
    .form-container {
      flex-direction: row;
      margin: 0;
      padding: 0;
      align-items: center;
    }
    .form-label {
      display: flex;
      flex-direction: row;
      align-items: center;
      margin-bottom: 0px;
    }
    .form-label:nth-child(even) {
      margin-left: 10px;
    }
    .form-label:nth-child(odd) {
      margin-right: 10px;
    }
  }
</style>
<div>
  <form class="form-container">
    <div class="form-label">
      <label for="votesToWin">
        Votes to Win (1-9999):
      </label>
      <input
        id="votesToWin"
        type="number"
        min="1"
        max="9999"
        step="1"
        bind:value={raceConfig.votesToWin}
        on:input={event => handleInput('votesToWin', event)}
      />
    </div>
    <div class="form-label">
      <label for="autoStep">
        Auto Step every N seconds<br/>(0 for manual step):
      </label>
      <input
        id="autoStep"
        type="number"
        min="0"
        max="9999"
        step="1"
        bind:value={raceConfig.autoStep}
        on:input={event => handleInput('autoStep', event)}
      />
    </div>
  </form>
</div>

