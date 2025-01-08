<template>
  <div id="dashboard" class="h-full">
    <!-- PASTE IFRAME SNIPPET HERE-->
    <iframe
      style="
        background: #21313c;
        border: none;
        border-radius: 2px;
        box-shadow: 0 2px 10px 0 rgba(70, 76, 79, 0.2);
        width: 100vw;
        height: 100vh;
      "
      src="https://charts.mongodb.com/charts-project-0-dxalyto/embed/dashboards?id=95a41794-80d9-4f2f-89cc-55ea7b7a8e25&theme=dark&autoRefresh=true&maxDataAge=3600&showTitleAndDesc=true&scalingWidth=fixed&scalingHeight=fixed"
    ></iframe>
  </div>
</template>

<script>
export default {
  name: "DashboardPage",
};
</script>

<style scoped>
/* Add your styles here */
</style>