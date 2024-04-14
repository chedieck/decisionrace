<script lang="ts">
  import { onMount } from 'svelte';

  type Option = {
    id: number;
    name: string;
    votes: number;
  };

  function getTitle(name: string, votes: number): string {
    return `${name} (${votes}/${VOTES_TO_WIN})`;
  }

  let minWidth = 20; // Default minWidth
  let finished = false;
  export let optionNames: string[] = [];
  let options: Option[] = [];
  const VOTES_TO_WIN: number = 20;

  onMount(() => {
    options = optionNames.map((option, index) => ({ id: index, name: option, votes: 0 }));
    updateMinWidth();
  });

  function updateMinWidth(): void {
    minWidth = Math.max(
      ...options.map(option => getTitle(option.name, VOTES_TO_WIN).length),
      minWidth
    );
    // Convert to a more manageable unit if necessary, e.g., assuming each character takes roughly 0.6ch space
    minWidth *= 1;
  }

  function raceStep(): void {
    if (finished) return;
    const selected: number = Math.floor(Math.random() * options.length);
    options[selected].votes = Math.min(options[selected].votes + 1, VOTES_TO_WIN); // Prevent exceeding VOTES_TO_WIN
    if (options[selected].votes >= VOTES_TO_WIN) {
      titleMessage = `🏆 ${options[selected].name} won the race! 🏆`;
      finished = true
    }
  }

  let titleMessage = 'The race has started!';
  function handleKeydown(event: KeyboardEvent) {
    if (event.key === ' ' || event.key === 'Enter') {
      raceStep();
    }
  }

  onMount(() => {
    window.addEventListener('keydown', handleKeydown);
    return () => {
      window.removeEventListener('keydown', handleKeydown);
    };
  });
</script>

<style>
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
  .title {
    width: 100%;
    min-width: 100%;
  }

  .score {
    font-size: 24px;
    font-weight: bold;
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
    max-height: 90vh;
  }

  .items-container {
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 84vh;
  }

  .item-container:nth-child(even) {
    background-color: var(--color-bg-1);
  }
</style>

<div class="race-container">
  <h1 class="title">{titleMessage}</h1>
  <div class="items-container">
    {#each options as { id, name, votes }}
      <div style='height: {Math.trunc(100/options.length)}%;' class="item-container">
        <div class="option-title">
          <div class="score">{votes.toString().padStart(2, '0')}/{VOTES_TO_WIN}</div>

          <div class="name">{name}</div>
          <div></div>
        </div>
        <div class="track">
          <div class="progress-container">
            <div class="progress-bar" style={`width: ${(votes / VOTES_TO_WIN) * 100}%`}>
            </div>
            <div class={`horse ${votes === VOTES_TO_WIN ? 'horse-won' : ''}`}>🐎</div>
          </div>
          <div class="finish-line">🏁</div>
        </div>
      </div>
    {/each}
  </div>
</div>

{#if !finished}
  <button on:click={raceStep}>Next Step</button>
{/if}

