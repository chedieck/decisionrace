<script>
  import ChoiceSelector from '$lib/components/ChoiceSelector.svelte'


  const author = "Estevão Chedieck Lobo"

  const url = "https://race.chedieck.com"

  const title = "DecisionRace — Turn random decisions into a thrilling race."

  const description = "Settle decisions between which options to pick. Whether it's choosing tonight's movie, the next book club read, where to dine, or who gets the last cookie in the pack, DecisionRace adds excitement to every choice."

  const keywords = "Decision, Decision Making, Choices, Fun, Race, Entertainment, Interactive, Games, Decision Help, Choice Assistance, Random Choice, Random, Decicions, Choice, Help Choosing"
</script>

<svelte:head>
	<!-- Primary Meta Tags -->
	<title>DecisionRace</title>
	<meta charset="UTF-8"/>
	<meta name="title" content={title}/>
	<meta name="description" content={description}/>

	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
	<meta name="keywords" content={keywords}/>
	<meta name="author" content={author}/>
	<meta name="language" content="English"/>
	<link rel="canonical" href={url}/>
	<!-- Social Media Tags -->

	<meta property="og:type" content="website"/>
	<meta property="og:url" content={url}/>
	<meta property="og:title" content={title}/>
	<meta property="og:description" content={description}/>
  <meta property="og:image" content={`${url}/1200x630-facebook.png`}/>

	<!-- Twitter Card data -->
  <meta name="twitter:image" content={`${url}/1200x628-twitter.png`}/>
	<meta name="twitter:card" content="summary_large_image"/>
	<meta name="twitter:title" content={title}/>
	<meta name="twitter:description" content={description}/>


</svelte:head>

<div class="page">
	<ChoiceSelector/>
</div>

<style>
	.page {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-between;
	}
</style>
