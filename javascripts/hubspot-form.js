// HubSpot Newsletter Form Initialization
document.addEventListener("DOMContentLoaded", function () {
  var formContainer = document.getElementById("hubspot-newsletter-form");

  if (formContainer && window.hbspt && window.hbspt.forms) {
    window.hbspt.forms.create({
      portalId: "242432742",
      formId: "df4190b8-3804-4c1e-98c6-f73625ef5d01",
      region: "na2",
      css: "",
      target: "#hubspot-newsletter-form",
    });
  }
});
