/* Base JavaScript File for Florida Beach Insider */
$(function () {
  
  /* * * Google Analytics Custom Stuff * * */
  //Select any link that links to Priceline page; track as event
  $("a[href*='secure.rezserver.com']").click(function(e){
    e.preventDefault();
    var link = $(this).attr("href");
    var path = window.location.pathname;
    var clickedOn = $(this).attr("data-ga-label");
    //Send event to GA
    ga('send', {
      'hitType': 'event',
      'eventCategory': 'Priceline click-through',
      'eventAction': 'Click',
      'eventLabel': path+"#"+clickedOn
    });
    //Wait for event to track
    setTimeout(loadPage, 333);
    //Redirect to outbound page
    function loadPage() {
      window.open(link, '_blank');
    }
  });

  //Mobile menu
  $("#navMenu").click(function () {
    $("#navLinks").toggleClass("open");
  });

  //What's New?
  whatsNew();

  //Header scroll effect
  scrollHeader();

  //Profile subnav
  //Scroll to ID
  $("body").on("click", ".subnav-element", function () {
    var linkID = $(this).attr("data-scroll");
    $('html,body').animate({
      scrollTop: ($("#" + linkID).offset().top) - 130
    });
    $(".subnav-elements, #subnavOpener").removeClass("open");
  });

  $("#subnavOpener").click(function () {
    $(this).toggleClass("open");
    $(".subnav-elements").toggleClass("open");
  });
  $("body").on("click", ".subnav-opener-static", function () {
    $(".sticky-subnav.peek").toggleClass("poke");
    $(this).toggleClass("poke");
  });
  //Clone subnav
  $("#subnavElements").clone().appendTo("#stickySubnav");

  //Beach Filters
  beachFilters();
  
  $("input#EBFname").keyup(function () {
    beachFilters();
  });
  $("select#EBFmetro, select#EBFregion, select#EBFcounty, .beach-feature").change(function () {
    beachFilters();
  });
  //Open hidden features checklist
  $( "#EBFattributes" ).click( function () {
    $( "#exploreBeachesAttributes" ).toggleClass( "open-attributes" );
  } );

});

$(window).resize(function () {
  whatsNew();
  $(".subnav-elements, #subnavOpener").removeClass("open");
});

//Header scroll effect
$(window).scroll(function () {
  scrollHeader();
  //Profile subnav
  if ($("#subnav").length > 0) {
    var dST = $(document).scrollTop();
    var pST = $("#subnav").offset().top;
    var pH = $("#subnav").outerHeight();
    if ((pST + pH) < dST) {
      $("#stickySubnav").addClass("peek");
    } else {
      $("#stickySubnav").removeClass("peek");
    }
  }
});

function whatsNew() {
  //Get location and size of What's New? nav element
  var wnT = $("#navWhatsNew").position().top;
  var wnL = $("#navWhatsNew").position().left;
  var wnW = $("#navWhatsNew").outerWidth();
  var wnH = $("#navWhatsNew").outerHeight();
  var nT = wnT + ((wnH / 2) - 60);
  var nL = wnL + ((wnW / 2) - 60);

  $("#whatsNew").css({
    top: nT + "px",
    left: nL + "px"
  });
}

function scrollHeader() {
  if (!$("#header").hasClass("stay-scrolled")) {
    var st = $(this).scrollTop();
    if (st > 100) {
      $("#header, #headerSocialFlyin").addClass("scrolled");
    } else {
      $("#header, #headerSocialFlyin").removeClass("scrolled");
    }
  }
}

function beachFilters() {

  var EBFterm;
  if($("input#EBFname").length > 0){
    if($("input#EBFname").val().length > 0){
      EBFterm = $("input#EBFname").val().toLowerCase();
    } else {
      EBFterm = "";
    }
  }
  var EBFmetro = $("select#EBFmetro").val().toLowerCase();
  var EBFcounty = $("select#EBFcounty").val().toLowerCase();
  var EBFregion = $("select#EBFregion").val().toLowerCase();
  var iC = 0;
  var beachTerms, hideBeach, featureList;
  //Loop through beaches
  $(".explore-beach").each(function () {
    hideBeach = false;
    //Check against search term input
    if ($(this).attr("data-terms")) {
      beachTerms = $(this).attr("data-terms").toLowerCase();
      if (beachTerms.indexOf(EBFterm) < 0) {
        hideBeach = true;
      } else {
        iC++;
      }
    }
    //Check against Metro select input
    if ($(this).attr("data-metro")) {
      if (EBFmetro !== "all") {
        if ($(this).attr("data-metro").toLowerCase().indexOf(EBFmetro) < 0) {
          hideBeach = true;
        } else {
          iC++;
        }
      }
    }
    //Check against County select input
    if ($(this).attr("data-county")) {
      if (EBFcounty !== "all") {
        if ($(this).attr("data-county").toLowerCase().indexOf(EBFcounty) < 0) {
          hideBeach = true;
        } else {
          iC++;
        }
      }
    }
    //Check against Regions select input
    if ($(this).attr("data-region")) {
      if (EBFregion !== "all") {
        if ($(this).attr("data-region").toLowerCase().indexOf(EBFregion) < 0) {
          hideBeach = true;
        } else {
          iC++;
        }
      }
    }

    //Check against features
    featureList = $(this).attr("data-features");
    if ($(".beach-feature:checked").length > 0) {
      $(".beach-feature").each(function (i) {
        if ($(this).attr("id") === "feature" + i && $(this).is(":checked") && featureList.substr(i, 1) === "0") {
          hideBeach = true;
        } else {
          iC++;
        }
      });
    }

    if (hideBeach) {
      $(this).addClass("explore-beach-hidden");
    } else {
      $(this).removeClass("explore-beach-hidden");
    }
    if (iC < 1) {
      $("#noResults").addClass("show-no-results");
    } else {
      $("#noResults").removeClass("show-no-results");
    }

  });
}
