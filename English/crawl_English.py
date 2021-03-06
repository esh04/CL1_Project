import requests
from bs4 import BeautifulSoup

filename = "English_data.txt"
with open(filename, 'a') as txtfile:
   
    urls = ['https://www.nytimes.com/2021/06/28/world/asia/india-covid-oxygen.html?searchResultPosition=16','https://www.nytimes.com/2021/06/12/world/asia/india-modi-covid.html?searchResultPosition=15','https://www.nytimes.com/2021/06/08/world/pilots-india-covid-compensation.html?searchResultPosition=14','https://www.nytimes.com/2021/06/17/opinion/india-covid-ganges.html?searchResultPosition=12','https://www.nytimes.com/2021/06/24/podcasts/the-daily/serum-institute-coronavirus-vaccine.html?searchResultPosition=10','https://www.nytimes.com/2021/06/22/world/india-covid-vaccination.html?searchResultPosition=9','https://www.nytimes.com/2021/05/06/us/india-covid-telehealth-dalits.html?searchResultPosition=6','https://www.nytimes.com/2021/05/09/world/india-covid-mucormycosis.html?searchResultPosition=5','https://www.nytimes.com/2021/05/27/technology/india-twitter.html?searchResultPosition=30','https://www.nytimes.com/interactive/2021/05/25/world/asia/india-covid-death-estimates.html?searchResultPosition=29','https://www.nytimes.com/2021/06/17/world/south-asia-covid-vaccines.html?searchResultPosition=18','https://www.nytimes.com/2021/05/28/opinion/covid-vaccine-variants.html?searchResultPosition=28','https://www.nytimes.com/2021/05/30/world/asia/nepal-covid19-migrants.html?searchResultPosition=27','https://www.nytimes.com/2021/05/28/world/asia/india-covid-vaccine-pfizer.html?searchResultPosition=26','https://www.nytimes.com/2021/05/31/world/asia/india-covid.html?searchResultPosition=25','https://www.nytimes.com/2021/05/31/health/covid-variant-names-india-delta.html?searchResultPosition=23','https://www.nytimes.com/2021/06/03/technology/india-israel-facebook-employees.html?searchResultPosition=22','https://www.nytimes.com/2021/06/03/us/coronavirus-vaccine-college-students.html?searchResultPosition=21','https://www.nytimes.com/2021/04/29/world/asia/india-coronavirus-vaccines.html?searchResultPosition=20','https://www.nytimes.com/2021/05/01/world/asia/india-covid19-modi.html?searchResultPosition=19','https://www.nytimes.com/2021/05/16/world/asia/india-covid19-black-market.html?searchResultPosition=4','https://www.nytimes.com/2021/05/13/world/asia/covid19-india-nepal-bangladesh-sri-lanka.html?searchResultPosition=3','https://www.nytimes.com/2021/06/20/world/asia/india-covid-black-fungus.html?searchResultPosition=2','https://www.nytimes.com/2021/05/25/world/asia/india-covid-experience.html?searchResultPosition=1']
  
    for url in urls:
        res = requests.get(url)
        html_page = res.content

        soup = BeautifulSoup(html_page, 'html.parser')
        #texts = soup.find_all("p")
        #texts = soup.find_all("p", {"dir": "ltr"})
        #texts = soup.find_all("p", {"class": "paywall"})
        texts = soup.find_all("p", {"class": "css-axufdj evys1bk0"})
        #texts = soup.find_all("p", {"class": "f-body"})

        for text in texts:
            txtfile.write(text.get_text())
        print("done")
        
 #urls
 # https://www.wired.com/story/delta-coronavirus-variant-low-vaccine-rates-could-spike-cases/
 # https://www.wired.co.uk/article/china-coronavirus
 # https://www.wired.com/story/the-teeny-tiny-scientific-screwup-that-helped-covid-kill/
 # https://www.wired.co.uk/article/covid-19-uk-third-wave
 # https://www.medicalnewstoday.com/articles/wired-healthtech-2020-latest-advances-and-the-fight-against-covid-19#How-does-the-world-feel-about-vaccines?
 # https://www.wired.com/story/us-vaccine-milestone-india-shots-coronavirus-news/
 # https://www.wired.com/story/vaccine-incentives-surplus-doses-coronavirus-news/
 # https://www.wired.com/story/the-uk-has-a-plan-for-a-new-pandemic-radar-system/
 # https://www.wired.com/story/the-challenge-of-covid-19-vaccines-for-the-immunosuppressed/
 # https://www.wired.com/story/wear-your-vaccinated-sticker-with-pride/
 # https://www.wired.com/story/no-covid-19-vaccines-wont-make-you-magnetic-heres-why/
 # https://www.wired.com/story/vaccinations-slow-americans-travel-coronavirus-news/

 # p tag
 # https://www.the-scientist.com/news-opinion/new-evidence-shows-covid-19-was-in-us-weeks-before-thought-68906
 # https://www.the-scientist.com/news-opinion/two-new-coronaviruses-make-the-leap-into-humans-68783
 # https://www.ndtv.com/world-news/coronavirus-delta-variant-forces-new-lockdowns-as-europe-lifts-covid-restrictions-2473157
 # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7090728/
# https://www.nature.com/articles/d41586-020-00502-w


# paywall
# https://www.wired.com/story/coronavirus-guide-faq-advice/
# https://www.wired.com/story/100-million-vaccines-new-school-guidelines-coronavirus-news/
# https://www.wired.com/story/shot-approval-transmission-coronavirus-news/
# https://www.wired.com/story/heres-a-plan-to-stop-the-coronavirus-from-mutating/
# https://www.wired.com/story/as-coronavirus-variants-spread-the-us-struggles-to-keep-up/
# https://www.wired.com/story/the-first-shots-grim-milestones-coronavirus-news/


# https://www.masterstudies.com/article/what-students-should-know-about-the-coronavirus/

# nytimes
# 'https://www.nytimes.com/2021/06/23/science/coronavirus-sequences.html?searchResultPosition=1'
# 'https://www.nytimes.com/2021/06/22/health/delta-variant-covid.html?searchResultPosition=2'
# 'https://www.nytimes.com/2021/06/20/science/covid-lab-leak-wuhan.html?searchResultPosition=3'
# 'https://www.nytimes.com/2021/06/07/health/covid-alpha-uk-variant.html?searchResultPosition=4'
# 'https://www.nytimes.com/2021/06/20/health/covid-drugs-peptide-vitamins.html?searchResultPosition=5'
# 'https://www.nytimes.com/2021/06/17/health/covid-pill-antiviral.html?searchResultPosition=6'
# 'https://www.nytimes.com/2021/05/27/health/wuhan-coronavirus-lab-leak.html?searchResultPosition=12'
# 'https://www.nytimes.com/2021/05/13/health/vaccine-pregnancy.html?searchResultPosition=14'
# 'https://www.nytimes.com/2021/05/14/health/coronavirus-variants-united-states-of-america.html?searchResultPosition=15'
# 'https://www.nytimes.com/2021/05/11/health/covid-tests-flu.html?searchResultPosition=16'
# 'https://www.nytimes.com/2021/05/12/us/covid-pandemic.html?searchResultPosition=18'
# 'https://www.nytimes.com/2021/05/12/parenting/vaccine-children.html?searchResultPosition=19'
# 'https://www.nytimes.com/2021/04/22/health/covid-vaccines-rates-men-and-women.html?searchResultPosition=22'
# 'https://www.nytimes.com/interactive/2021/04/17/travel/flying-plane-covid-19-safety.html?searchResultPosition=23'
# 'https://www.nytimes.com/2021/04/17/health/covid-convalescent-plasma.html?searchResultPosition=24'
# 'https://www.nytimes.com/2021/04/16/health/johnson-vaccine-blood-clot-case.html?searchResultPosition=25'
# 'https://www.nytimes.com/2021/06/24/us/coronavirus-briefing-what-happened-today.html?searchResultPosition=26'
# 'https://www.nytimes.com/2021/06/22/opinion/lab-leak-covid.html?searchResultPosition=27'
# 'https://www.nytimes.com/2021/06/21/us/coronavirus-briefing-what-happened-today.html?searchResultPosition=28'
# 'https://www.nytimes.com/2021/06/15/us/coronavirus-california-timeline.html?searchResultPosition=29'
# 'https://www.nytimes.com/2021/06/25/us/politics/supreme-court-alaska-tribes-virus.html?searchResultPosition=30'
# 'https://www.nytimes.com/2021/06/24/science/ancient-coronavirus-epidemic.html?searchResultPosition=31'
# 'https://www.nytimes.com/2021/04/14/health/cdc-johnson-vaccine-pause.html?searchResultPosition=32'
# 'https://www.nytimes.com/2021/06/25/opinion/coronavirus-lab.html?searchResultPosition=34'
# 'https://www.nytimes.com/2021/06/15/health/coronavirus-usa-cases.html?searchResultPosition=35'
# 'https://www.nytimes.com/2021/06/24/world/europe/covid-vaccine-mix-and-match-pfizer-moderna.html?searchResultPosition=39'
# 'https://www.nytimes.com/2021/06/08/us/coronavirus-briefing-what-happened-today.html?searchResultPosition=40'
# 'https://www.nytimes.com/2021/04/13/health/blood-clots-johnson-vaccine.html?searchResultPosition=41'
# 'https://www.nytimes.com/2021/06/07/us/coronavirus-today-vaccines.html?searchResultPosition=46'
# 'https://www.nytimes.com/2021/06/03/us/coronavirus-briefing-what-happened-today.html?searchResultPosition=48'
# 'https://www.nytimes.com/2021/06/03/world/africa/africa-coronavirus-cases.html?searchResultPosition=49'
# 'https://www.nytimes.com/2021/06/27/opinion/covid-vaccine-variants.html?searchResultPosition=51'
# 'https://www.nytimes.com/2021/06/28/health/coronavirus-vaccines-immunity.html?searchResultPosition=53'
# 'https://www.nytimes.com/2021/06/26/realestate/can-my-building-ask-residents-for-proof-of-vaccination.html?searchResultPosition=54'
# 'https://www.nytimes.com/2021/06/26/world/sydney-lockdown-covid.html?searchResultPosition=57'
# 'https://www.nytimes.com/2021/06/24/world/us-covid-cases-nih.html?searchResultPosition=58'
# 'https://www.nytimes.com/2021/06/28/world/astrazeneca-vaccine-booster-shot.html?searchResultPosition=60'
# 'https://www.nytimes.com/2021/06/28/world/asia/bangladesh-lockdown.html?searchResultPosition=62'
# 'https://www.nytimes.com/2021/06/26/world/europe/matt-hancock-britain-resigns.html?searchResultPosition=63'
# 'https://www.nytimes.com/2021/06/24/world/us-covid-cases-nih.html?searchResultPosition=64'
# 'https://www.nytimes.com/2021/06/27/world/asia/covid-mount-everest-nepal.html?searchResultPosition=65'
# 'https://www.nytimes.com/2021/06/27/world/asia/covid-mount-everest-nepal.html?searchResultPosition=65'
# 'https://www.nytimes.com/2021/06/25/us/louisiana-covid-vaccination-lottery.html?searchResultPosition=77'
# 'https://www.nytimes.com/2021/06/26/us/western-us-vaccine-covid.html?searchResultPosition=79'
# 'https://www.nytimes.com/2021/06/25/world/europe/blinken-france-china-macron.html?searchResultPosition=80'
# 'https://www.nytimes.com/2021/06/23/world/secret-service-covid-trump.html?searchResultPosition=81'
# 'https://www.nytimes.com/2021/06/24/us/politics/biden-vaccines.html?searchResultPosition=83'
# 'https://www.nytimes.com/2021/06/26/health/covid-vaccine-teens-consent.html?searchResultPosition=86'
# 'https://www.nytimes.com/2021/06/24/nyregion/nyc-tourism.html?searchResultPosition=87'

# p
# https://pharmaceutical-journal.com/article/feature/everything-you-should-know-about-the-coronavirus-outbreak
# https://www.ncbi.nlm.nih.gov/books/NBK554776/
# 'https://www.frontiersin.org/articles/10.3389/fmed.2020.00250/full'

# f-body
# 'https://www.nejm.org/doi/full/10.1056/NEJMsr2105280?query=featured_coronavirus'
# 'https://www.nejm.org/doi/full/10.1056/NEJMc2108861?query=featured_coronavirus'
# 'https://www.nejm.org/doi/full/10.1056/NEJMoa2101544?query=featured_coronavirus'
# 'https://www.nejm.org/doi/full/10.1056/NEJMc2107717?query=featured_coronavirus'
# 'https://www.nejm.org/doi/full/10.1056/NEJMoa2101765?query=featured_coronavirus'
# 'https://www.nejm.org/doi/full/10.1056/NEJMc2103916?query=featured_coronavirus'
# 'https://www.nejm.org/doi/full/10.1056/NEJMc2101927?query=featured_coronavirus'

# wiki
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic'
# 'https://en.wikipedia.org/wiki/Coronavirus'
# 'https://en.wikipedia.org/wiki/COVID-19'
# 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India'
# https://en.wikipedia.org/wiki/COVID-19_vaccine

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7239068/

# 'https://www.nature.com/articles/d41586-020-03626-1'
# 'https://emedicine.medscape.com/article/2500139-overview'
# 'https://www.nature.com/articles/s41418-020-00720-9
# 'https://jbiomedsci.biomedcentral.com/articles/10.1186/s12929-020-00695-2'

# 'https://www.health.harvard.edu/diseases-and-conditions/preventing-the-spread-of-the-coronavirus'

# nytimes
# 'https://www.nytimes.com/2020/12/08/health/covid-vaccine-mask.html?pageType=LegacyCollection&collectionName=Covid-19+Vaccines&label=Covid-19+Vaccines&module=hub_Band&region=inline&template=storyline_band_recirc'
# 'https://www.nytimes.com/2020/12/24/health/herd-immunity-covid-coronavirus.html?pageType=LegacyCollection&collectionName=Covid-19+Vaccines&label=Covid-19+Vaccines&module=hub_Band&region=inline&template=storyline_band_recirc'
# 'https://www.nytimes.com/2020/12/05/health/covid-vaccine-first.html?pageType=LegacyCollection&collectionName=Covid-19+Vaccines&label=Covid-19+Vaccines&module=hub_Band&region=inline&template=storyline_band_recirc'
# 'https://www.nytimes.com/2021/06/28/health/mixing-pfizer-astrazeneca-results.html?pageType=LegacyCollection&collectionName=Covid-19+Vaccines&label=Covid-19+Vaccines&module=hub_Band&region=inline&template=storyline_band_recirc'
# 'https://www.nytimes.com/2021/06/08/health/us-vaccines-children-fall.html'

# p
# 'https://www.sciencemag.org/news/2021/06/claim-chinese-team-hid-early-sars-cov-2-sequences-stymie-origin-hunt-sparks-furor'
# 'https://www.sciencemag.org/news/2021/06/delta-variant-triggers-dangerous-new-phase-pandemic'
# 'https://www.sciencemag.org/news/2021/06/gives-hope-third-covid-19-vaccine-dose-can-boost-protection-organ-transplant-recipients'
# 'https://www.sciencemag.org/news/2021/06/brazil-gives-russian-covid-19-vaccine-chance-approving-import-limited-doses'
# 'https://www.sciencemag.org/news/2021/06/powerful-new-covid-19-vaccine-shows-90-efficacy-could-boost-worlds-supply'
# 'https://www.sciencemag.org/news/2021/06/landmark-trial-test-mrna-vaccines-against-covid-19-africa-can-t-get-coveted-shots'
# 'https://www.sciencemag.org/news/2021/06/would-you-have-your-dna-tested-predict-how-hard-covid-19-would-strike-should-you'
# 'https://www.sciencemag.org/news/2021/06/tragic-spring-surge-leads-india-crank-coronavirus-vaccine-effort'
# 'https://www.sciencemag.org/news/2021/06/brazilian-town-experiment-shows-mass-vaccination-can-wipe-out-covid-19'
# 'https://www.sciencemag.org/news/2021/06/israel-reports-link-between-rare-cases-heart-inflammation-and-covid-19-vaccination'
# 'https://www.sciencemag.org/news/2021/05/biden-adds-voice-calls-further-investigation-origins-pandemic-virus'
# 'https://www.sciencemag.org/news/2021/05/antivaccine-activists-use-government-database-side-effects-scare-public'
# 'https://www.sciencemag.org/news/2021/05/rich-countries-cornered-covid-19-vaccine-doses-four-strategies-right-scandalous'
# 'https://www.sciencemag.org/news/2021/05/i-m-subject-nl002-0060-and-i-m-dropping-out-my-covid-19-vaccine-trial'
# 'https://www.sciencemag.org/news/2021/05/two-more-coronaviruses-can-infect-people-studies-suggest'
# https://journals.lww.com/pidj/fulltext/2005/11001/history_and_recent_advances_in_coronavirus.12.aspx
# 'https://www.mayoclinic.org/diseases-conditions/coronavirus/expert-answers/novel-coronavirus/faq-20478727'
# 'https://www.mayoclinic.org/diseases-conditions/coronavirus/expert-answers/visits-after-covid-19-vaccination/faq-20506463'
# 'https://www.mayoclinic.org/diseases-conditions/coronavirus/expert-answers/can-coronavirus-spread-food-water/faq-20485479'
# 'https://www.mayoclinic.org/diseases-conditions/coronavirus/expert-answers/coronavirus-and-vitamin-d/faq-20493088'
# 'https://www.mayoclinic.org/tests-procedures/convalescent-plasma-therapy/about/pac-20486440'
# 'https://www.mayoclinic.org/diseases-conditions/coronavirus/in-depth/coronavirus-safety-tips/art-20485967'
# 'https://www.mayoclinic.org/diseases-conditions/coronavirus/symptoms-causes/syc-20479963'
# 'https://www.mayoclinic.org/diseases-conditions/coronavirus/in-depth/coping-with-coronavirus-grief/art-20486392'

#nytimes
# 'https://www.nytimes.com/2021/06/17/world/americas/vancouver-couple-vaccine-guilty.html?searchResultPosition=26'
# 'https://www.nytimes.com/2021/06/27/opinion/covid-vaccine-variants.html?searchResultPosition=28'
# 'https://www.nytimes.com/article/vaccine-covid-card.html?searchResultPosition=30'
# 'https://www.nytimes.com/2021/06/17/us/coronavirus-deaths-vaccines.html?searchResultPosition=25'
# 'https://www.nytimes.com/2021/06/23/world/white-house-brazil-covid-vaccine-doses.html?searchResultPosition=24'
# 'https://www.nytimes.com/2021/06/27/world/brazil-covid-vaccine.html?searchResultPosition=23'
# 'https://www.nytimes.com/2021/06/22/us/houston-hospital-covid-vaccine.html?searchResultPosition=22'
# 'https://www.nytimes.com/2021/06/16/us/emergent-biosolutions-covid-vaccine.html?searchResultPosition=19'
# 'https://www.nytimes.com/2021/06/22/world/americas/cuba-vaccine-abdala.html?searchResultPosition=17'
# 'https://www.nytimes.com/2021/06/28/health/coronavirus-vaccines-immunity.html?searchResultPosition=13'
# 'https://www.nytimes.com/article/vaccine-passport.html?searchResultPosition=7'
# 'https://www.nytimes.com/2021/06/22/business/economy/china-vaccines-covid-outbreak.html?searchResultPosition=5'
# 'https://www.nytimes.com/2021/06/24/opinion/covid-vaccine-doctor-nurse.html?searchResultPosition=4'
# 'https://www.nytimes.com/2021/06/22/business/morgan-stanley-vaccination-requirement.html?searchResultPosition=3'
# 'https://www.nytimes.com/2021/06/24/podcasts/the-daily/serum-institute-coronavirus-vaccine.html?searchResultPosition=2'

# 'https://www.nytimes.com/2021/06/28/world/asia/india-covid-oxygen.html?searchResultPosition=16'
# 'https://www.nytimes.com/2021/06/12/world/asia/india-modi-covid.html?searchResultPosition=15'
# 'https://www.nytimes.com/2021/06/08/world/pilots-india-covid-compensation.html?searchResultPosition=14'
# 'https://www.nytimes.com/2021/06/17/opinion/india-covid-ganges.html?searchResultPosition=12'
# 'https://www.nytimes.com/2021/06/24/podcasts/the-daily/serum-institute-coronavirus-vaccine.html?searchResultPosition=10'
# 'https://www.nytimes.com/2021/06/22/world/india-covid-vaccination.html?searchResultPosition=9'
# 'https://www.nytimes.com/2021/05/06/us/india-covid-telehealth-dalits.html?searchResultPosition=6'
# 'https://www.nytimes.com/2021/05/09/world/india-covid-mucormycosis.html?searchResultPosition=5'
# 'https://www.nytimes.com/2021/05/27/technology/india-twitter.html?searchResultPosition=30'
# 'https://www.nytimes.com/interactive/2021/05/25/world/asia/india-covid-death-estimates.html?searchResultPosition=29'
# 'https://www.nytimes.com/2021/06/17/world/south-asia-covid-vaccines.html?searchResultPosition=18'
# 'https://www.nytimes.com/2021/05/28/opinion/covid-vaccine-variants.html?searchResultPosition=28'
# 'https://www.nytimes.com/2021/05/30/world/asia/nepal-covid19-migrants.html?searchResultPosition=27'
# 'https://www.nytimes.com/2021/05/28/world/asia/india-covid-vaccine-pfizer.html?searchResultPosition=26'
# 'https://www.nytimes.com/2021/05/31/world/asia/india-covid.html?searchResultPosition=25'
# 'https://www.nytimes.com/2021/05/31/health/covid-variant-names-india-delta.html?searchResultPosition=23'
# 'https://www.nytimes.com/2021/06/03/technology/india-israel-facebook-employees.html?searchResultPosition=22'
# 'https://www.nytimes.com/2021/06/03/us/coronavirus-vaccine-college-students.html?searchResultPosition=21'
# 'https://www.nytimes.com/2021/04/29/world/asia/india-coronavirus-vaccines.html?searchResultPosition=20'
# 'https://www.nytimes.com/2021/05/01/world/asia/india-covid19-modi.html?searchResultPosition=19'
# 'https://www.nytimes.com/2021/05/16/world/asia/india-covid19-black-market.html?searchResultPosition=4'
# 'https://www.nytimes.com/2021/05/13/world/asia/covid19-india-nepal-bangladesh-sri-lanka.html?searchResultPosition=3'
# 'https://www.nytimes.com/2021/06/20/world/asia/india-covid-black-fungus.html?searchResultPosition=2'
# 'https://www.nytimes.com/2021/05/25/world/asia/india-covid-experience.html?searchResultPosition=1'
