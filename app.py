from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    course_data = [
        {
            'title': 'Basic Spoken English',
            'description': 'Learn to speak English for everyday conversations.',
            'image': 'https://source.unsplash.com/300x200/?english,classroom',
            'link': 'https://basicenglishspeaking.com/'
        },
        {
            'title': 'Construction Safety Training',
            'description': 'Stay safe at your worksite with essential safety practices.',
            'image': 'https://source.unsplash.com/300x200/?construction,safety',
            'link': 'https://alison.com/course/construction-safety'
        },
        {
            'title': 'Learn Plumbing Basics',
            'description': 'Introduction to plumbing tools and techniques.',
            'image': 'https://source.unsplash.com/300x200/?plumbing,tools',
            'link': 'https://www.plumbworld.co.uk/blog/plumbing-basics-learn-about-your-home-plumbing-system'
        },
        {
            'title': 'Mobile Repair Training',
            'description': 'Hands-on repair course for mobile devices.',
            'image': 'https://source.unsplash.com/300x200/?mobile,repair',
            'link': 'https://www.udemy.com/course/mobile-repairing'
        },
        {
            'title': 'Farm Technology Essentials',
            'description': 'Know how to use modern tools in farming.',
            'image': 'https://source.unsplash.com/300x200/?farming,technology',
            'link': 'https://alison.com/tag/farming'
        },
        {
            'title': 'Domestic Electrician Course',
            'description': 'Training to become a certified home electrician.',
            'image': 'https://source.unsplash.com/300x200/?electrician,wires',
            'link': 'https://cursa.app/free-courses-electrician-online'
        }
    ]
    preview_courses = course_data[:3]

    news_items =[
    {
        "title": "Foreign workers help Spain's economic growth outpace the US and the rest of Europe",
        "summary": "Spain's economy has outpaced the US and Europe, largely due to foreign workers. With 45% of new jobs since 2022 filled by foreigners, they now comprise 13% of the workforce. This influx, mostly from Latin America, has bolstered Spain's economy, growing by 3% compared to the euro zone's 0.8% and the US's 2.8%.",
        "link": "https://apnews.com/article/c3abff0d83b60c9712fe4932b780eb21",
        "date": "March 2025"
    },
    {
        "title": "US labor groups sue over 'ignorant' cuts of programs fighting child labor abroad",
        "summary": "Several labor groups have filed a lawsuit against the Trump administration's termination of international labor rights programs. These programs aimed to combat child labor and uphold workers' rights globally.",
        "link": "https://www.theguardian.com/us-news/2025/apr/15/musk-doge-child-labor-cuts",
        "date": "April 15, 2025"
    },
    {
        "title": "An unexplained death, 'abuse and slavery': Indonesian fishers reveal life on long haul vessels",
        "summary": "Indonesian fishers report exploitation and abuse on foreign vessels, including harsh working conditions, physical violence, and inadequate food and medical care.",
        "link": "https://www.theguardian.com/global-development/2025/apr/01/crews-report-abuse-and-death-onboard-long-haul-vessels-seafood-industry",
        "date": "April 1, 2025"
    },
    {
        "title": "Don't allow you to go to the bathroom': big tech's call center workers in Greece on strike",
        "summary": "Call center workers in Greece employed by Teleperformance have gone on strike, accusing their employer of severe mistreatment, including retaliation against union organizers and restricted bathroom breaks.",
        "link": "https://www.theguardian.com/business/2025/jan/14/teleperformance-strike-greece-apple-google-netflix",
        "date": "January 14, 2025"
    },
    {
        "title": "Migrant worker dies at 2034 World Cup stadium in Saudi Arabia",
        "summary": "A Pakistani migrant worker died while working at the Aramco Stadium in Saudi Arabia, marking the first known death related to the construction of a 2034 World Cup stadium in the country.",
        "link": "https://www.thetimes.co.uk/article/migrant-worker-death-world-cup-saudi-arabia-8t2grd5gz",
        "date": "March 2025"
    },
    {
        "title": "Advancing social protection for migrant workers in the GCC countries: New ambition emerges from discussion at the Global Forum for Migration and Development Summit",
        "summary": "Officials and experts discuss pathways toward extending social protection to migrant workers in the Gulf region, with countries like Oman and Bahrain implementing reforms to enhance coverage.",
        "link": "https://www.ilo.org/resource/news/advancing-social-protection-migrant-workers-gcc-countries-new-ambition",
        "date": "February 1, 2024"
    }
]


    return render_template('home.html', preview_courses=preview_courses, news=news_items)


@app.route('/courses')
def courses():
    course_data = [
        {
            'title': 'Basic Spoken English',
            'description': 'Learn to speak English for everyday conversations.',
            'image': 'https://source.unsplash.com/300x200/?english,classroom',
            'link': 'https://basicenglishspeaking.com/'
        },
        {
            'title': 'Construction Safety Training',
            'description': 'Stay safe at your worksite with essential safety practices.',
            'image': 'https://source.unsplash.com/300x200/?construction,safety',
            'link': 'https://alison.com/course/construction-safety'
        },
        {
            'title': 'Learn Plumbing Basics',
            'description': 'Introduction to plumbing tools and techniques.',
            'image': 'https://source.unsplash.com/300x200/?plumbing,tools',
            'link': 'https://www.plumbworld.co.uk/blog/plumbing-basics-learn-about-your-home-plumbing-system'
        },
        {
            'title': 'Mobile Repair Training',
            'description': 'Hands-on repair course for mobile devices.',
            'image': 'https://source.unsplash.com/300x200/?mobile,repair',
            'link': 'https://www.udemy.com/course/mobile-repairing'
        },
        {
            'title': 'Farm Technology Essentials',
            'description': 'Know how to use modern tools in farming.',
            'image': 'https://source.unsplash.com/300x200/?farming,technology',
            'link': 'https://alison.com/tag/farming'
        },
        {
            'title': 'Domestic Electrician Course',
            'description': 'Training to become a certified home electrician.',
            'image': 'https://source.unsplash.com/300x200/?electrician,wires',
            'link': 'https://cursa.app/free-courses-electrician-online'
        }
    ]
    return render_template('courses.html', courses=course_data)


@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/helpline')
def helpline():
    return render_template('helpline.html')

if __name__ == '__main__':
    app.run(debug=True)
