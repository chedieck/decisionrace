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
  export let raceStarted: boolean

  let options: Option[] = [];
  const VOTES_TO_WIN: number = 20;

  function goBack() {
    raceStarted = false
  }

  function restart() {
    finished = false
    titleMessage = 'The race has started!';
    options = optionNames.map((option, index) => ({ id: index, name: option, votes: 0 }));
  }

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
      event.preventDefault()
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
    width: 100%;
    font-size: 2.5em;
    padding-top: 10px;
    padding-bottom: 20px;
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
    height: 84vh;
    border-top: solid 3px var(--color-text);
    border-bottom: solid 3px var(--color-text);
  }

  .item-container:nth-child(even) {
    background-color: var(--color-bg-1);
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
    visibility: hidden;
  }
  .tooltip-icon {
    border: solid 1px white;
    border-radius: 22px;
    padding: 4px;
  }

  .tooltip-container {
    position: absolute;
    right: 10%;
  }

  .tooltip-icon:hover + .tooltip {
    visibility: visible;
  }

  .question-mark {
    margin-left: 8px;
    cursor: pointer;
    font-size: 20px;
  }

</style>

<div class="race-container">
  <div class="title-container">
    <button on:click={goBack} style:visibility={finished ? 'visible' : 'hidden'}>
      Go back
    </button>
    <span class="title">{titleMessage}</span>
    <button on:click={restart} style:visibility={finished ? 'visible' : 'hidden'}>
      Restart
    </button>
  </div>
  <div class="items-container">
    {#each options as { id, name, votes }}
      <div style='height: {Math.trunc(90/options.length)}%;' class="item-container">
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
  <div style:visibility={finished ? 'hidden' : 'display'} class="center row bottom-button-container">
    <button class="next"  on:click={raceStep}>Next Step</button>
    <div class="tooltip-container">
      <span class="tooltip-icon">?</span>
      <span class="tooltip message">You can also press <kbd>Space</kbd> or <kbd>Enter</kbd> to take the next step.</span>
    </div>
  </div>

</div>
