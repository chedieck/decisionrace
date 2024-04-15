<script>
  import ChoiceSelector from '$lib/components/ChoiceSelector.svelte'
</script>

<svelte:head>
	<!-- Primary Meta Tags -->
	<title>Decision Race</title>
	<meta charset="UTF-8"/>
	<meta name="title" content="DecisionRace — Choosing made fun!"/>
	<meta name="description" content="Decision Race, the app where choices become a thrilling race! Perfect for settling decisions, picking options, or just for fun. Whether it's choosing tonight's movie, the next book club read, where to dine, or who gets the last cookie in the pack, Decision Race adds excitement to every choice. Visit race.chedieck.com and let the race begin!"/>

	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
	<meta name="keywords" content="Decision Making, Choices, Fun, Race, Entertainment, Interactive, Games, Decision Help, Choice Assistance"/>
	<meta name="author" content="Estevão Chedieck Lobo"/>
	<meta name="language" content="English"/>
	<link rel="canonical" href="https://race.chedieck.com"/>
	<!-- Social Media Tags -->

	<meta property="og:type" content="website"/>
	<meta property="og:url" content="https://race.chedieck.com"/>
	<meta property="og:title" content="DecisionRace — Choosing made fun!"/>
	<meta property="og:description" content="Decision Race, the app where choices become a thrilling race! Perfect for settling decisions, picking options, or just for fun. Visit race.chedieck.com and let the race begin!"/>
	<meta property="og:image" content="https://race.chedieck.com/1200x630-facebook.png"/>
	<!-- Twitter Card data -->
	<meta name="twitter:card" content="summary_large_image"/>
	<meta name="twitter:title" content="DecisionRace — Choosing made fun!"/>
	<meta name="twitter:description" content="Decision Race, the app where choices become a thrilling race! Perfect for settling decisions, picking options, or just for fun. Visit race.chedieck.com and let the race begin!"/>


</svelte:head>

<div class="page">
	<ChoiceSelector raceStarted={false}/>
</div>

<style>
	.page {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-between;
	}
</style>
