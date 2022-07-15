""" Video Link: https://youtu.be/1s-Tj65AKZA """
from seleniumbase import BaseCase


class HackTests(BaseCase):
    def test_all_your_base_are_belong_to_us(self):
        self.set_window_size(1220, 740)
        ayb = "ALL YOUR BASE"
        abtu = "ARE BELONG TO US"
        aybabtu = "%s %s" % (ayb, abtu)
        sb_banner_logo = "//seleniumbase.io/cdn/img/sb_logo_10.png"
        sb_dashboard_logo = "//seleniumbase.io/img/dash_pie_3.png"
        yt_chip = "#chips yt-chip-cloud-chip-renderer:nth-of-type"
        wiki = "https://en.wikipedia.org/wiki/All_your_base_are_belong_to_us"

        self.open(wiki)
        self.click_if_visible('button[aria-label="Close"]')
        self.set_text_content("h1#firstHeading", aybabtu)
        self.set_text_content("#ca-history a", aybabtu)
        self.set_text_content("#n-mainpage-description a", "ALL")
        self.set_text_content("#n-contents a", "YOUR")
        self.set_text_content("#n-currentevents a", "BASE")
        self.set_text_content("#n-randompage a", "ARE")
        self.set_text_content("#n-aboutsite a", "BELONG")
        self.set_text_content("#n-contactpage a", "TO")
        self.set_text_content("#n-sitesupport a", "US")
        self.set_text_content(".tocsection-1 span.toctext", "ALL")
        self.set_text_content(".tocsection-2 span.toctext", "YOUR")
        self.set_text_content(".tocsection-3 span.toctext", "BASE")
        self.set_text_content(".tocsection-4 span.toctext", "ARE")
        self.set_text_content(".tocsection-5 span.toctext", "BELONG")
        self.set_text_content(".tocsection-6 span.toctext", "TO")
        self.set_text_content(".tocsection-7 span.toctext", "US")
        self.highlight("h1#firstHeading", loops=2, scroll=False)
        self.highlight("#ca-history a", loops=2, scroll=False)
        self.highlight("nav#p-navigation", loops=2, scroll=False)
        self.highlight("div#toc", loops=2, scroll=False)
        self.highlight(".tocsection-1 span.toctext", loops=1, scroll=False)
        self.highlight(".tocsection-2 span.toctext", loops=1, scroll=False)
        self.highlight(".tocsection-3 span.toctext", loops=2, scroll=False)
        self.highlight(".tocsection-4 span.toctext", loops=1, scroll=False)
        self.highlight(".tocsection-5 span.toctext", loops=1, scroll=False)
        self.highlight(".tocsection-6 span.toctext", loops=1, scroll=False)
        self.highlight(".tocsection-7 span.toctext", loops=2, scroll=False)
        zoom_in = "div.thumbinner{zoom: 1.4;-moz-transform: scale(1.4);}"
        self.add_css_style(zoom_in)
        self.highlight("div.thumbinner", loops=8, scroll=False)

        if not self.headless:
            self.open("https://www.apple.com/store")
            self.set_text_content("div.rs-shop-subheader", aybabtu)
            self.set_text_content('#shelf-1 a[href*="mac"]', "ALL")
            self.set_text_content('#shelf-1 a[href*="iphone"]', "YOUR")
            self.set_text_content('#shelf-1 a[href*="ipad"]', "BASE")
            self.set_text_content('#shelf-1 a[href*="watch"]', "ARE")
            self.set_text_content('#shelf-1 a[href*="airpods"]', "BELONG")
            self.set_text_content('#shelf-1 a[href*="airtag"]', "TO")
            self.set_text_content('#shelf-1 a[href*="tv"]', "US")
            self.set_text_content('#shelf-1 a[href*="homepod"]', ".")
            self.set_text_content("h2", aybabtu + ". ")
            self.highlight("div.rs-shop-subheader", loops=6, scroll=False)
            self.highlight("#shelf-1", loops=2, scroll=False)
            self.highlight('#shelf-1 a[href*="mac"]', loops=1, scroll=False)
            self.highlight('#shelf-1 a[href*="iphone"]', loops=1, scroll=False)
            self.highlight('#shelf-1 a[href*="ipad"]', loops=3, scroll=False)
            self.highlight('#shelf-1 a[href*="watch"]', loops=1, scroll=False)
            self.highlight('#shelf-1 a[href*="airpod"]', loops=1, scroll=False)
            self.highlight('#shelf-1 a[href*="airtag"]', loops=1, scroll=False)
            self.highlight('#shelf-1 a[href*="tv"]', loops=3, scroll=False)
            self.highlight("h2", loops=9, scroll=False)

        self.open("https://google.com/ncr")
        self.hide_elements("iframe")
        self.set_text_content('a[href*="about.google"]', ayb)
        self.set_text_content('a[href*="store.google"]', abtu)
        self.set_text_content('a[href*="mail.google.com"]', ayb)
        self.set_text_content('a[href*="google.com/img"]', abtu)
        self.set_attributes('[value="Google Search"]', "value", ayb)
        self.set_attributes('[value="I\'m Feeling Lucky"]', "value", abtu)
        zoom_in = "a{zoom: 1.2;-moz-transform: scale(1.2);}"
        self.add_css_style(zoom_in)
        zoom_in = (
            '[value="ALL YOUR BASE"]{zoom: 1.3;-moz-transform: scale(1.3);}'
            '[value="ARE BELONG TO US"]{zoom: 1.3;-moz-transform: scale(1.3);}'
        )
        self.add_css_style(zoom_in)
        self.highlight('a[href*="about.google"]', loops=3)
        self.highlight('a[href*="store.google"]', loops=3)
        self.highlight('a[href*="mail.google.com"]', loops=3)
        self.highlight('a[href*="google.com/img"]', loops=3)
        self.highlight('form[role="search"]', loops=8)

        self.open("https://twitter.com/")
        if not self.is_element_visible('a[href*="w/signup"] span'):
            self.refresh()
        if self.is_element_visible('a[href*="w/signup"] span'):
            self.set_text_content('a[href*="w/signup"] span', aybabtu)
            self.highlight('a[href*="w/signup"] span', loops=6, scroll=False)
            self.highlight('a[href*="w/signup"]', loops=6, scroll=False)

        self.open("https://www.youtube.com/")
        self.set_text_content("%s(1)" % yt_chip, "ALL")
        self.set_text_content("%s(2)" % yt_chip, "YOUR")
        self.set_text_content("%s(3)" % yt_chip, "BASE")
        self.set_text_content("%s(4)" % yt_chip, "ARE")
        self.set_text_content("%s(5)" % yt_chip, "BELONG")
        self.set_text_content("%s(6)" % yt_chip, "TO")
        self.set_text_content("%s(7)" % yt_chip, "US")
        self.set_text_content("%s(8)" % yt_chip, "!")
        self.set_text_content("%s(9)" % yt_chip, "!")
        self.set_text_content("%s(10)" % yt_chip, "!")
        self.click_if_visible("#dismiss-button")
        self.click_if_visible('button[aria-label="Close"]')
        self.highlight("#scroll-container", loops=5, scroll=False)
        self.highlight("%s(1)" % yt_chip, loops=1, scroll=False)
        self.highlight("%s(2)" % yt_chip, loops=1, scroll=False)
        self.highlight("%s(3)" % yt_chip, loops=3, scroll=False)
        self.highlight("%s(4)" % yt_chip, loops=1, scroll=False)
        self.highlight("%s(5)" % yt_chip, loops=1, scroll=False)
        self.highlight("%s(6)" % yt_chip, loops=1, scroll=False)
        self.highlight("%s(7)" % yt_chip, loops=3, scroll=False)
        self.highlight("#scroll-container", loops=7, scroll=False)

        self.open("https://github.com/features/actions")
        self.set_text_content('a[href="/team"]', ayb)
        self.set_text_content('a[href="/enterprise"]', abtu)
        self.set_text_content("h1 span:nth-child(1)", ayb)
        self.set_text_content("h1 span:nth-of-type(2)", "ARE")
        self.set_text_content("h1 span:nth-of-type(3)", "BELONG")
        self.set_text_content("h1 span:nth-of-type(4)", "TO")
        self.set_text_content("h1 span:nth-of-type(5)", "US")
        self.type('input[name="q"]', aybabtu.lower())
        self.click("h1", scroll=False)
        self.highlight("nav", loops=5, scroll=False)
        self.highlight('input[name="q"]', loops=5, scroll=False)
        self.highlight("h1", loops=8, scroll=False)

        self.open("https://dev.to/top/infinity")
        self.click_if_visible('button[aria-label="Close campaign banner"]')
        self.set_text_content('nav a[data-text="Relevant"]', "ALL")
        self.set_text_content('nav a[data-text="Latest"]', "YOUR")
        self.set_text_content('nav a[data-text="Top"]', "BASE")
        self.set_text_content('nav a[data-text="Week"]', "ARE")
        self.set_text_content('nav a[data-text="Month"]', "BELONG")
        self.set_text_content('nav a[data-text="Year"]', "TO")
        self.set_text_content('nav a[data-text="Infinity"]', "US")
        self.set_text_content('aside a[class*="tful"]', aybabtu)
        self.set_text_content('aside a[aria-label="Create new account"]', ayb)
        self.set_text_content('aside a[aria-label="Log in"]', abtu)
        self.set_text_content('aside a[class*="tful"]:nth-child(2)', aybabtu)
        self.set_text_content('aside a[class*="tful"]:nth-child(3)', aybabtu)
        self.set_text_content('aside a[class*="tful"]:nth-child(4)', aybabtu)
        self.set_text_content('aside a[class*="tful"]:nth-child(5)', aybabtu)
        self.set_attribute("a.crayons-avatar img", "src", sb_dashboard_logo)
        self.set_text_content(".profile-preview-card button", "SeleniumBase")
        self.set_text_content("h2.crayons-story__title a", aybabtu)
        self.type('input[name="q"]', aybabtu)
        self.highlight('input[name="q"]', loops=4, scroll=False)
        self.highlight('[aria-label="Primary sidebar"] div div', scroll=False)
        self.highlight('nav a[data-text="Relevant"]', loops=1, scroll=False)
        self.highlight('nav a[data-text="Latest"]', loops=1, scroll=False)
        self.highlight('nav a[data-text="Top"]', loops=2, scroll=False)
        self.highlight('nav a[data-text="Week"]', loops=1, scroll=False)
        self.highlight('nav a[data-text="Month"]', loops=1, scroll=False)
        self.highlight('nav a[data-text="Year"]', loops=1, scroll=False)
        self.highlight('nav a[data-text="Infinity"]', loops=2, scroll=False)
        self.highlight('aside[id*="sidebar"] section', loops=5, scroll=False)
        self.highlight("div.crayons-story__body", loops=7, scroll=False)

        self.open("https://azure.microsoft.com/en-us/services/playfab/")
        self.set_text_content("h1", aybabtu)
        self.set_text_content('a[aria-label*="Try PlayF"]', ayb)
        self.set_text_content('a[aria-label*="Sign in to"]', abtu)
        self.highlight("h1", loops=6, scroll=False)
        self.highlight('a[aria-label*="Try PlayF"]', loops=4, scroll=False)
        self.highlight('a[aria-label*="Sign in to"]', loops=6, scroll=False)

        self.open("https://store.steampowered.com/")
        self.set_text_content('div.content a[href*="/about/"]', " ")
        self.set_text_content('div.content a[href*="help.steam"]', aybabtu)
        self.set_text_content("#foryou_tab a", "ALL")
        self.set_text_content("#noteworthy_tab a", "YOUR BASE")
        self.set_text_content("#genre_tab a", "ARE")
        self.set_text_content('span:contains("Points Shop")', "BELONG")
        self.set_text_content('span:contains("News")', "TO")
        self.set_text_content('span:contains("Labs")', "US")
        self.set_value("input#store_nav_search_term", ayb + " . . . .")
        self.highlight('div.content a[href*="help.steam"]', loops=6)
        self.highlight("#store_nav_area", loops=2, scroll=False)
        self.highlight("#foryou_tab a", loops=1, scroll=False)
        self.highlight("#noteworthy_tab a", loops=3, scroll=False)
        self.highlight("#genre_tab a", loops=1, scroll=False)
        self.highlight('span:contains("BELONG")', loops=1, scroll=False)
        self.highlight('span:contains("TO")', loops=1, scroll=False)
        self.highlight('span:contains("US")', loops=2, scroll=False)
        self.js_click('input[id*="nav_search"]')
        self.highlight('input[id*="nav_search"]', loops=6, scroll=False)

        self.open("https://xkcd.com/286/")
        self.set_text_content('a[href="/archive"]', "ALL")
        self.set_text_content('a[href*="what-if"]', "YOUR")
        self.set_text_content('a[href*="//blag."]', "BASE")
        self.set_text_content('a[href*="/about"]', abtu)
        self.remove_element('li:contains("Feed")')
        self.remove_element('li:contains("TW")')
        self.remove_element('li:contains("Books")')
        self.remove_element('li:contains("What")')
        self.remove_element('li:contains("WI")')
        self.set_attributes("#news img", "src", sb_banner_logo)
        self.set_text_content("#ctitle", aybabtu)
        self.set_text_content('a[rel="prev"]', "All")
        self.set_text_content('a[href*="random"]', "Your")
        self.set_text_content('a[rel="next"]', "Base")
        self.highlight("#topLeft ul", loops=5, scroll=False)
        self.highlight('a[href="/archive"]', loops=1, scroll=False)
        self.highlight('a[href*="what-if"]', loops=1, scroll=False)
        self.highlight('a[href*="//blag."]', loops=2, scroll=False)
        self.highlight('a[href*="/about"]', loops=5, scroll=False)
        self.highlight('a[rel="prev"]', loops=1, scroll=False)
        self.highlight('a[href*="random"]', loops=1, scroll=False)
        self.highlight('a[rel="next"]', loops=3, scroll=False)
        self.highlight("#ctitle", loops=7, scroll=False)

        self.open("https://www.nintendo.com/whatsnew/")
        self.set_text_content("h1", aybabtu)
        self.highlight("h1", loops=10, scroll=False)

        if not self.headless:
            self.open("https://support.gog.com/hc/en-us?product=gog")
            self.set_text_content("div.intro-title", aybabtu)
            self.set_text_content("h4", aybabtu)
            self.highlight("div.intro-title", loops=8, scroll=False)
            self.highlight("h4", loops=8, scroll=False)

        self.open("https://slack.com/help/articles/204714258-Giphy-for-Slack")
        self.set_text_content("h1", aybabtu)
        self.set_text_content('a[prettyslug="getting-started"]', "ALL")
        self.set_text_content('a[prettyslug="using-slack"]', "YOUR")
        self.set_text_content('a[prettyslug="your-profile"]', "BASE")
        self.set_text_content('a[prettyslug="connect-tools"]', "ARE")
        self.set_text_content('a[prettyslug="administration"]', "BELONG")
        self.set_text_content('a[prettyslug="tutorials"]', "TO US")
        self.highlight("h1", loops=4, scroll=False)
        self.highlight("div#global_menu", loops=2, scroll=False)
        self.highlight('a[prettyslug*="g-started"]', loops=1, scroll=False)
        self.highlight('a[prettyslug="using-slack"]', loops=1, scroll=False)
        self.highlight('a[prettyslug="your-profile"]', loops=2, scroll=False)
        self.highlight('a[prettyslug="connect-tools"]', loops=1, scroll=False)
        self.highlight('a[prettyslug="administration"]', loops=1, scroll=False)
        self.highlight('a[prettyslug="tutorials"]', loops=2, scroll=False)

        self.open("https://kubernetes.io/")
        self.set_text_content('nav a[href="/docs/"]', "ALL")
        self.set_text_content('nav a[href="/blog/"]', "YOUR")
        self.set_text_content('nav a[href="/training/"]', "BASE")
        self.set_text_content('nav a[href="/partners/"]', "ARE")
        self.set_text_content('nav a[href="/community/"]', "BELONG")
        self.set_text_content('nav a[href="/case-studies/"]', "TO")
        self.set_text_content("nav #navbarDropdown", "US")
        self.set_text_content("nav #navbarDropdownMenuLink", ".")
        if self.is_element_visible("h1"):
            self.set_text_content("h1", aybabtu)
        self.highlight("nav ul.navbar-nav", loops=3, scroll=False)
        self.highlight('nav a[href="/docs/"]', loops=1, scroll=False)
        self.highlight('nav a[href="/blog/"]', loops=1, scroll=False)
        self.highlight('nav a[href="/training/"]', loops=2, scroll=False)
        self.highlight('nav a[href="/partners/"]', loops=1, scroll=False)
        self.highlight('nav a[href="/community/"]', loops=1, scroll=False)
        self.highlight('nav a[href="/case-studies/"]', loops=1, scroll=False)
        self.highlight("nav #navbarDropdown", loops=2, scroll=False)
        if self.is_element_visible("h1"):
            self.highlight("h1", loops=6, scroll=False)

        self.open("https://www.selenium.dev/")
        if self.is_element_visible('button[data-dismiss="alert"] span'):
            self.js_click('button[data-dismiss="alert"] span', scroll=False)
        self.set_attributes("a.dropdown-toggle", "class", "nav-link")
        self.set_text_content('li a:contains("About")', "ALL")
        self.set_text_content('li a:contains("Downloads")', "YOUR")
        self.set_text_content('li a:contains("Documentation")', "BASE")
        self.set_text_content('li a:contains("Projects")', "ARE")
        self.set_text_content('li a:contains("Support")', "BELONG")
        self.set_text_content('li a:contains("Blog")', "TO")
        self.set_text_content('li a:contains("English")', "US")
        self.set_text_content("div.lead", aybabtu)
        self.set_text_content("h2", aybabtu)
        zoom_in = "div.lead{zoom: 1.25;-moz-transform: scale(1.25);}"
        self.add_css_style(zoom_in)
        self.highlight("div#main_navbar", loops=1, scroll=False)
        self.highlight('li a:contains("ALL")', loops=1, scroll=False)
        self.highlight('li a:contains("YOUR")', loops=1, scroll=False)
        self.highlight('li a:contains("BASE")', loops=2, scroll=False)
        self.highlight('li a:contains("ARE")', loops=1, scroll=False)
        self.highlight('li a:contains("BELONG")', loops=1, scroll=False)
        self.highlight('li a:contains("TO")', loops=1, scroll=False)
        self.highlight('li a:contains("US")', loops=2, scroll=False)
        self.highlight("div.lead", loops=6, scroll=False)
        self.highlight("h2", loops=8, scroll=False)

        self.open("https://www.python.org/")
        self.set_text_content('a[class="donate-button"]', ayb)
        self.set_text_content("#about a", "ALL")
        self.set_text_content("#downloads a", "YOUR")
        self.set_text_content("#documentation a", "BASE")
        self.set_text_content("#community a", "ARE")
        self.set_text_content("#success-stories a", "BELONG")
        self.set_text_content("#news a", "TO")
        self.set_text_content("#events a", "US")
        self.highlight('a[class="donate-button"]', loops=4, scroll=False)
        self.highlight("nav#mainnav", loops=5, scroll=False)
        self.highlight("#about a", loops=1, scroll=False)
        self.highlight("#downloads a", loops=1, scroll=False)
        self.highlight("#documentation a", loops=2, scroll=False)
        self.highlight("#community a", loops=1, scroll=False)
        self.highlight("#success-stories a", loops=1, scroll=False)
        self.highlight("#news a", loops=1, scroll=False)
        self.highlight("#events a", loops=2, scroll=False)

        self.open("https://docs.pytest.org/")
        self.set_text_content("h1", "pytest: " + aybabtu)
        self.highlight("h1", loops=10, scroll=False)

        self.open("https://wordpress.com/")
        self.set_text_content('a[title="Plans & Pricing"]', aybabtu)
        self.set_text_content('a[title="Get Started"]', ayb)
        self.set_text_content("p.no-widows", aybabtu)
        self.set_text_content("a#lpc-button", "Automate with SeleniumBase")
        self.highlight('a[title="Plans & Pricing"]', loops=6, scroll=False)
        self.highlight('a[title="Get Started"]', loops=4, scroll=False)
        self.highlight("p.no-widows", loops=8, scroll=False)
        self.highlight("a#lpc-button", loops=4, scroll=False)

        self.open("https://seleniumbase.com/")
        self.set_text_content("h1", aybabtu)
        self.highlight("h1", loops=10, scroll=False)

        self.open("https://pypi.org/")
        self.set_text_content('a[href="/sponsors/"]', aybabtu)
        self.set_text_content("h1", aybabtu)
        self.set_value("input#search", aybabtu, scroll=False)
        self.highlight('a[href="/sponsors/"]', loops=6, scroll=False)
        self.highlight("h1", loops=6, scroll=False)
        self.highlight("input#search", loops=8, scroll=False)

        self.open("https://www.atlassian.com/software/jira")
        self.set_text_content('a[href*="jira/pricing"]', ayb)
        self.set_text_content('a[href*="jira/enterprise"]', abtu)
        self.set_text_content('a[href="/software/jira/features"]', "")
        self.set_text_content('a[href="/software/jira/guides"]', "")
        self.set_text_content("h1", aybabtu)
        self.highlight("ul.imkt-navbar__link-list", loops=2, scroll=False)
        self.highlight('a[href*="jira/pricing"]', loops=3, scroll=False)
        self.highlight('a[href*="jira/enterprise"]', loops=3, scroll=False)
        self.highlight("h1", loops=6, scroll=False)

        self.open("https://status.iboss.com/ibcloud/app/cloudStatus.html")
        self.set_text_content('div[translate*="cloudStatus"]', ayb)
        self.set_text_content('div[translate*="maintenance"]', "ARE")
        self.set_text_content('div[translate*="advisory"]', "BELONG")
        self.set_text_content('div[translate*="incident"]', "TO US")
        self.set_text_content("h1", "Cloud Status - " + aybabtu)
        self.highlight("nav div.ibcloud-header-contents", loops=3)
        self.highlight('div[translate*="cloudStatus"]', loops=4)
        self.highlight('div[translate*="maintenance"]', loops=1)
        self.highlight('div[translate*="advisory"]', loops=1)
        self.highlight('div[translate*="incident"]', loops=3)
        self.highlight("h1", loops=9, scroll=False)

        self.open("https://git-scm.com/")
        self.set_text_content("span#tagline", aybabtu)
        self.set_text_content("#nav-about h3", ayb)
        self.set_text_content("#nav-documentation h3", abtu)
        self.highlight("span#tagline", loops=8, scroll=False)
        self.highlight("#nav-about h3", loops=5, scroll=False)
        self.highlight("#nav-documentation h3", loops=6, scroll=False)

        self.open("https://teamtreehouse.com/teams")
        self.set_text_content("li.nav-item-free-trial", aybabtu)
        self.set_text_content("h1", aybabtu)
        self.set_text_content("h2", aybabtu)
        self.set_text_content("p.homepage-signup-form-banner", aybabtu)
        self.highlight("li.nav-item-free-trial", loops=6, scroll=False)
        self.highlight("h1", loops=6, scroll=False)
        self.highlight('p[class*="signup-form"]', loops=6, scroll=False)

        self.open("https://pragprog.com/")
        self.set_text_content("header p", aybabtu)
        zoom_in = "header p{zoom: 1.35;-moz-transform: scale(1.35);}"
        self.add_css_style(zoom_in)
        self.highlight("header p", loops=10, scroll=False)

        self.open("https://seleniumbase.io/")
        self.set_text_content("h1", aybabtu)
        self.highlight("h1", loops=10, scroll=False)
