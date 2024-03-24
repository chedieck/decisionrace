<script>
  import ChoiceSelector from '../components/ChoiceSelector.svelte'
	import banner from '$lib/images/banner.png';
</script>

<svelte:head>
	<!-- Primary Meta Tags -->
	<title>Decision Race</title>
	<meta charset="UTF-8"/>
	<meta name="title" content="Decision Race - Make Choices Fun"/>
	<meta name="description" content="Decision Race, the app where choices become a thrilling race! Perfect for settling decisions, picking options, or just for fun. Whether it's choosing tonight's movie, the next book club read, where to dine, or who gets the last cookie in the pack, Decision Race adds excitement to every choice. Visit decisionrace.com and let the race begin!"/>

	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
	<meta name="keywords" content="Decision Making, Choices, Fun, Race, Entertainment, Interactive, Games, Decision Help, Choice Assistance"/>
	<meta name="author" content="Estevão Chedieck Lobo"/>
	<meta name="language" content="English"/>
	<link rel="canonical" href="https://www.decisionrace.com"/>
	<!-- Social Media Tags -->

	<meta property="og:type" content="website"/>
	<meta property="og:url" content="https://www.decisionrace.com"/>
	<meta property="og:title" content="Decision Race - Make Choices Fun"/>
	<meta property="og:description" content="Decision Race, the app where choices become a thrilling race! Perfect for settling decisions, picking options, or just for fun. Visit decisionrace.com and let the race begin!"/>
	<meta property="og:image" content="https://www.decisionrace.com/1200x630-facebook.png"/>
	<!-- Twitter Card data -->
	<meta name="twitter:card" content="summary_large_image"/>
	<meta name="twitter:title" content="Decision Race - Make Choices Fun"/>
	<meta name="twitter:description" content="Decision Race, the app where choices become a thrilling race! Perfect for settling decisions, picking options, or just for fun. Visit decisionrace.com and let the race begin!"/>
	<meta name="twitter:image" content="U/1200x628-twitter.png"/>


</svelte:head>

<section>
  <!--
		<span class="banner">
			<picture>
				<img src={banner} alt="Welcome" />
			</picture>
		</span>
      -->
	<ChoiceSelector/>
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.5;
	}

	h1 {
		width: 100%;
	}

	.banner {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.banner img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
