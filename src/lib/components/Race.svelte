<script lang="ts">
  import { onMount } from 'svelte';
	import type { RaceConfigType, OptionType } from '$lib/types';

  export let optionNames: string[] = [];
  export let raceStarted: boolean
  export let raceConfig: RaceConfigType

  function getTitle(name: string, votes: number): string {
    return `${name} (${votes}/${raceConfig.votesToWin})`;
  }

  let minWidth = 20; // Default minWidth
  let finished = false;
  let timerId: number
  let secondCounterId: number
  let lastExecutionTime: number = (new Date()).getTime()

  let timerSeconds = raceConfig.autoStep
  let options: OptionType[] = [];

  function goBack() {
    raceStarted = false
  }

  function restart() {
    clearInterval(timerId);
    clearInterval(secondCounterId);

    options = optionNames.map((option, index) => ({ id: index, name: option, votes: 0 }));

    if (raceConfig.autoStep > 0) {
      lastExecutionTime = Date.now();
      timerId = setInterval(raceStep, raceConfig.autoStep * 1000);
      secondCounterId = setInterval(secondCounter, 1000);
      timerSeconds = raceConfig.autoStep;
    }

    finished = false;
    titleMessage = 'The race has started!';
  }

  function secondCounter() {
    const currentTime = Date.now();
    const elapsedTime = (currentTime - lastExecutionTime) / 1000; // elapsed time in seconds
    timerSeconds = raceConfig.autoStep - Math.floor(elapsedTime);

    if (timerSeconds <= 0) {
      lastExecutionTime = currentTime; // Reset last execution time at the end of the countdown
      timerSeconds = raceConfig.autoStep; // Reset timerSeconds
    }
  }


  onMount(() => {
    options = optionNames.map((option, index) => ({ id: index, name: option, votes: 0 }));
    updateMinWidth();
  });

  function updateMinWidth(): void {
    minWidth = Math.max(
      ...options.map(option => getTitle(option.name, raceConfig.votesToWin).length),
      minWidth
    );
    // Convert to a more manageable unit if necessary, e.g., assuming each character takes roughly 0.6ch space
    minWidth *= 1;
  }

  function raceStep(): void {
    if (finished) return;
    const selected: number = Math.floor(Math.random() * options.length);
    options[selected].votes = Math.min(options[selected].votes + 1, raceConfig.votesToWin); // Prevent exceeding
    if (options[selected].votes >= raceConfig.votesToWin) {
      titleMessage = `🏆 ${options[selected].name} won the race! 🏆`;
      finished = true
    }
    lastExecutionTime = (new Date()).getTime()
  }

  let titleMessage = 'The race has started!';
  function handleKeydown(event: KeyboardEvent) {
    if (event.key === ' ' || event.key === 'Enter') {
      event.preventDefault()
      raceStep();
    }
  }

  onMount(() => {
    if (raceConfig.autoStep > 0) {
      secondCounterId = setInterval(secondCounter, 1000);
      timerId = setInterval(raceStep, raceConfig.autoStep * 1000);
    } else {
      window.addEventListener('keydown', handleKeydown);
      return () => {
        clearInterval(timerId)
        window.removeEventListener('keydown', handleKeydown);
      };
    }
  });

</script>

<style>
  button {
    cursor: pointer;
    width: 20%;
    font-size: 16px;
    border-radius: 0;
  }

  .item-container {
    padding: 5px;
    flex: 1;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  .track {
    width: 100%;
    height: 100%;
    display: flex;
    position: absolute;
    top: 0;
    left: 0;
    align-items: center;
    padding-left: 20px;
    border-radius: 10px;
    font-size: 36px;
  }

  .option-title {
    width: 100%;
    display: flex;
    position: absolute;
    top: 0;
    left: 0;
    align-items: center;
    justify-content: space-between;
    height: 100%;
    transition: width 0.5s ease;
    text-align: center;
  }

  .name {
    font-size: 24px;
    align-content: center;
  }

  .progress-bar {
    height: 100%;
    transition: width 0.5s ease;
    text-align: center;
  }
  .horse {
    z-index: 100;
    transform: translateX(150%); /* Move horse outside the progress bar when it reaches 100% */
  }

  .horse-won {
    transform: translateX(200%); /* Move horse outside the progress bar when it reaches 100% */
  }

  .finish-line {
    height: 100%;
    display: flex;
    flex-direction: row;
    text-align: center;
    align-items: center;
    padding-right: 30px;
  }

  .title-container {
    display: flex;
    height: 10vh;
    flex-direction: row;
    justify-content: space-around;
    text-align: center;
    align-items: center;
  }

  .title {
    font-size: 2.5em;
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .score {
    font-size: 24px;
    font-weight: bold;
    padding-left: 12px;
  }

  .item-container:nth-child(odd) {
    background-color: var(--color-bg-2);
  }

  .progress-container {
    width: 90%;
    display: flex;
    overflow: visible;
  }

  .race-container {
    width: 100%;
  }

  .items-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 81vh;
    border-top: solid 3px var(--color-text);
  }

  .item-container:nth-child(even) {
    background-color: var(--color-bg-1);
  }

  .top-button {
    height: 61%;
    width: 10%;
  }

  .bottom-button-container {
    height: 5vh;
    justify-content: space-around;
  }

  .next {
    padding: 4px;
  }

  .tooltip {
    font-size: 16px;
    align-items: center;
    text-align: center;
  }

  .tooltip-container {
    display: none;
  }

  @media (min-width: 769px) {
    .next {
      display: none; /* Hide the button on PC */
    }
    .tooltip-container {
      display: block; /* Show the tooltip on PC */
    }
  }

  /* Media query for mobile devices (screens up to 768px wide) */
  @media (max-width: 768px) {
    .tooltip-container {
      display: none; /* Hide the tooltip on mobile */
    }
  }

</style>

<div class="race-container">
  <div class="title-container">
    <button class="top-button" on:click={goBack}>
      Go back
    </button>
    <span class="title">{titleMessage}</span>
    <button class="top-button" on:click={restart}>
      Restart
    </button>
  </div>
  <div class="items-container">
    {#each options as { id, name, votes }}
      <div style='height: {Math.trunc(90/options.length)}%;' class="item-container">
        <div class="option-title">
          <div class="score">{votes.toString().padStart(2, '0')}/{raceConfig.votesToWin.toString().padStart(2, '0')}</div>

          <div class="name">{name}</div>
          <div></div>
        </div>
        <div class="track">
          <div class="progress-container">
            <div class="progress-bar" style={`width: ${(votes / raceConfig.votesToWin) * 100}%`}>
            </div>
            <div class={`horse ${votes === raceConfig.votesToWin ? 'horse-won' : ''}`}>🐎</div>
          </div>
          <div class="finish-line">🏁</div>
        </div>
      </div>
    {/each}
  </div>
  {#if raceConfig.autoStep > 0 && timerSeconds !== undefined}
    <div style:visibility={finished? 'hidden' : 'display'} class="center row bottom-button-container">
      Next step in {timerSeconds} seconds...
    </div>
  {:else}
    <div style:visibility={finished? 'hidden' : 'display'} class="center row bottom-button-container">
      <button class="next"  on:click={raceStep}>Next Step</button>
      <div class="tooltip-container">
        <span class="tooltip message">Press <kbd>Space</kbd> or <kbd>⏎ Enter</kbd> to take the next step.</span>
      </div>
    </div>
  {/if}

</div>
