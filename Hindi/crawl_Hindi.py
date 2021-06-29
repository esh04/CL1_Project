import requests
from bs4 import BeautifulSoup

filename = "Hindi_data2.txt"
with open(filename, 'a') as txtfile:
    urls=['https://www.hindisahityadarpan.in/2016/10/mahabharat-hindi-complete-story.html','https://www.hindisahityadarpan.in/2016/10/mahabharat-aadi-parv-in-hindi.html','https://www.hindisahityadarpan.in/2016/10/sabha-parv-mahabharat-hindi.html','https://www.hindisahityadarpan.in/2017/04/van-parv-mahabharat-stories-hindi.html','https://www.hindisahityadarpan.in/2017/04/virat-parv-mahabharat-stories-in-hindi.html','https://www.hindisahityadarpan.in/2017/04/udyog-parv-mahabharat-stories-in-hindi.html','https://www.hindisahityadarpan.in/2017/04/bheeshm-parv-mahabharat-stories-in-hindi.html','https://www.hindisahityadarpan.in/2017/04/dron-parv-mahabharat-stories-hindi.html','https://www.hindisahityadarpan.in/2017/05/Karna-parv-mahabharat-stories-hindi.html','https://www.hindisahityadarpan.in/2017/05/Shalya-Parv-Mahabharat-Stories-Hindi.html','https://www.hindisahityadarpan.in/2017/05/Souptik-Parva-Mahabharat-Stories-Hindi.html','https://www.hindisahityadarpan.in/2017/05/stree-parva-mahabharat-stories-hindi.html','https://www.hindisahityadarpan.in/2017/05/shanti-parv-mahabharat-stories-in-hindi.html','https://www.hindisahityadarpan.in/2017/05/anushasan-parv-mahabharata-in-hindi.html','https://www.hindisahityadarpan.in/2017/05/aashwamedhik-parv-mahabharat-stories-hindi.html','https://www.hindisahityadarpan.in/2017/05/aashramvasik-parv-mahabharat-stories-hindi.html','https://www.hindisahityadarpan.in/2017/05/mausal-parv-mahabharat-stories.html','https://www.hindisahityadarpan.in/2017/05/mahaprasthanik-parv-mahabharat-hindi.html','https://www.hindisahityadarpan.in/2017/05/swargarohan-parv-mahabharat-stories-hindi.html']
    for url in urls:
        res = requests.get(url)
        html_page = res.content

        soup = BeautifulSoup(html_page, 'html.parser')

        #texts = soup.find_all("span", {"lang": "HI"})
        #texts = soup.find_all("span",{"style":"font-family: inherit;"})
        texts = soup.find_all("p",{"style":"text-align: justify;"})
        #texts = soup.find_all("p")
        
        for text in texts:
            txtfile.write(text.get_text())
        print("done")

#urls used
# 'https://www.hindisahityadarpan.in/2016/10/mahabharat-hindi-complete-story.html'
# 'https://www.hindisahityadarpan.in/2016/10/mahabharat-aadi-parv-in-hindi.html'
# 'https://www.hindisahityadarpan.in/2016/10/sabha-parv-mahabharat-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/04/van-parv-mahabharat-stories-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/04/virat-parv-mahabharat-stories-in-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/04/udyog-parv-mahabharat-stories-in-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/04/bheeshm-parv-mahabharat-stories-in-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/04/dron-parv-mahabharat-stories-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/Karna-parv-mahabharat-stories-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/Shalya-Parv-Mahabharat-Stories-Hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/Souptik-Parva-Mahabharat-Stories-Hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/stree-parva-mahabharat-stories-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/shanti-parv-mahabharat-stories-in-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/anushasan-parv-mahabharata-in-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/aashwamedhik-parv-mahabharat-stories-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/aashramvasik-parv-mahabharat-stories-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/mausal-parv-mahabharat-stories.html'
# 'https://www.hindisahityadarpan.in/2017/05/mahaprasthanik-parv-mahabharat-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/swargarohan-parv-mahabharat-stories-hindi.html'
#https://www.hindisahityadarpan.in/2017/06/yaksha-yudhisthir-samvad-story-mahabharat-hindi.html
# 'https://www.hindisahityadarpan.in/2017/05/birth-of-karna-story-from-mahabharat-hindi.html'
# 'https://www.hindisahityadarpan.in/2017/05/friendship-of-karna-duryodhana-story.html'
# 'https://www.hindisahityadarpan.in/2017/06/varnavat-conspiracy-story-mahabharat-hindi.html'

# 'https://www.hindisahityadarpan.in/2017/05/birth-of-bheeshm-and-bheeshm-pratigya.html'
# 'https://www.hindisahityadarpan.in/2017/05/story-eklavya-mahabharat-hindi.html'

# 'https://www.patrika.com/astrology-and-spirituality/what-happened-to-pandavas-and-shri-krishna-after-mahabharata-2266936/'
# 'https://www.thepublic.in/religion-hinduism/mahabharata/mahabharat-yudh-ki-samapti-end-of-mahabharat-war-mahabharat-yudh-in-hindi-mahabharat-yudh-story-in-hindi-mahabharat-yudh-fullmahabharat-yudh-ki-samapti-mahabharat-katha-in-hindi'

# 'https://www.ajabgjab.com/2014/08/how-did-shri-krishna-die.html'
# 'https://www.ajabgjab.com/2014/07/why-pandavas-had-eaten-body-of-his-dead.html'
# 'https://www.ajabgjab.com/2014/08/history-of-mythological-naga-snake.html'
# 'https://www.ajabgjab.com/2014/11/how-to-get-bheema-1000-elephants-power.html'
# 'https://www.ajabgjab.com/2014/11/urvashi-cursed-arjun.html'
# 'https://hindi.webdunia.com/mahabharat/story-after-mahabharat-war-in-hindi-118080800058_1.html'
#https://hindi.vedapusthakan.net/2016/11/17/abraham-genesis-15-hindi/?gclid=CjwKCAjwieuGBhAsEiwA1Ly_nQ1tTrNBb6d_UI0mewivbACdWlIHP8hgMPiNiyWA9gConI3N4_cowhoCZxoQAvD_BwE

# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%BE%E0%A4%B0%E0%A5%8B%E0%A4%B9%E0%A4%A3_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_2_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-20'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%BE%E0%A4%B0%E0%A5%8B%E0%A4%B9%E0%A4%A3_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_3_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-20'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%BE%E0%A4%B0%E0%A5%8B%E0%A4%B9%E0%A4%A3_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_4_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-23'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%B5%E0%A4%B0%E0%A5%8D%E0%A4%97%E0%A4%BE%E0%A4%B0%E0%A5%8B%E0%A4%B9%E0%A4%A3_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_5_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-20'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8%E0%A4%BF%E0%A4%95_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_1_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-21'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8%E0%A4%BF%E0%A4%95_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_2_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-26'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E2%80%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8%E0%A4%BF%E0%A4%95_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_3_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-16'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_1_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-16'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_2_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-17'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_3_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-16'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_4_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-12'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_5_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-15'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_6_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-18'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_7_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-18'
# 'https://hi.krishnakosh.org/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3/%E0%A4%AE%E0%A4%B9%E0%A4%BE%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4_%E0%A4%AE%E0%A5%8C%E0%A4%B8%E0%A4%B2_%E0%A4%AA%E0%A4%B0%E0%A5%8D%E0%A4%B5_%E0%A4%85%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF_8_%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%8B%E0%A4%95_1-15'
#https://roar.media/hindi/main/mythology/surviving-warriors-after-the-mahabharata-hindi-article
# 'https://www.mehtvta.com/essay-mahabharat-hindi/'
#'https://visionindiafoundation.com/draupadi-mahabharata-feminism-hindi/'
# 'https://isha.sadhguru.org/in/hi/wisdom/article/mahabharat-ke-yuddh-ka-kaaran-bana-yh-juye-ka-khel'
#'https://www.gyanmanthan.net/secret-of-mahabharat-in-hindi/'
