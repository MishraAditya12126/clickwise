import streamlit as st
st.balloons()
st.title(':violet[CLICK]-WISE 👆')
tab1,tab2,tab3,tab4,tab5 = st.tabs(['About us','How we do it?','What service we provide','Team members','Contact Us'])
with tab1:
    col1,col2 = st.columns(2)
    with col1:
        st.subheader('What is *:violet[CLICK]-WISE*?')
        st.write('''We are a team of Social Media Marketing Agency (SMMA) is a business that specializes in providing social media marketing and
        advertising services to other businesses and individuals. 
        Our Company i.e. :violet[CLICK]-WISE help their clients improve their online presence, engage with their target audience,
        and ultimately achieve their marketing and business objectives through various social media platforms.''')
    with col2:
        st.image('market.jpg')

    st.write('''
    Social Media Marketing Agencies are at the forefront of the ever-evolving world of social media. They stay up-to-date with the latest trends, algorithms, and best practices on platforms like Facebook, Instagram, Twitter, LinkedIn, and TikTok, ensuring that their clients can effectively navigate the dynamic landscape of digital marketing. By harnessing the power of social media, these agencies help businesses build meaningful connections with their audience, drive website traffic, boost sales, and enhance their online reputation, making them a crucial asset in the modern digital marketing ecosystem.
    ''')
    st.write('''Social Media Marketing Agencies often work with a diverse range of industries and customize their strategies to meet the unique needs and objectives of each client. Their expertise can be invaluable in improving brand awareness, customer engagement, and ultimately, driving business growth through social media platforms.
    ''')

with tab2:
    st.subheader('What *:red[steps]* do we follow ?')
    st.write('1.:blue[Market Research]:')
    st.write('''Understand your target market by identifying demographics, preferences, behaviors, and needs.
                Analyze your competitors to determine what sets your product or service apart.''')
    st.divider()
    st.write('2.:blue[Set Clear Objectives]:')
    st.write('''Define specific, measurable, achievable, relevant, and time-bound (SMART) marketing objectives.
Determine what you want to achieve, whether it's brand awareness, lead generation, sales, or something else.''')
    st.divider()
    st.write('3.:blue[Develop a Marketing Strategy]:')
    st.write('''Create a comprehensive marketing strategy that outlines the overall plan for achieving your objectives.
Decide on the marketing channels, tactics, and messaging that will be most effective.''')
    st.divider()
    st.write('4.:blue[Budget Allocation]:')
    st.write('''Allocate your budget to different marketing activities and channels based on their expected ROI.''')
    st.divider()
    st.write('5.:blue[Content Creation]:')
    st.write('''Develop high-quality content, including blog posts, videos, graphics, and other materials that resonate with your target audience.''')
    st.divider()
    st.write('6.:blue[Choose Marketing Channels]:')
    st.write(
        '''Select the marketing channels that best reach your audience, such as social media, email marketing, search engine optimization (SEO), pay-per-click advertising, content marketing, and more.''')
    st.divider()
    st.write('7.:blue[Execute the Plan]:')
    st.write('''Implement your marketing strategy and launch campaigns across selected channels.
Ensure consistent messaging and branding across all channels.''')
    st.divider()
    st.write('8.:blue[Analyze and Monitor]:')
    st.write('''Continuously track the performance of your marketing campaigns.
Use analytics tools to measure key metrics like website traffic, conversion rates, engagement, and sales.''')
    st.divider()
    st.write('9.:blue[Adjust and Optimize]:')
    st.write('''Based on the data and insights gathered, make adjustments to your marketing strategy.
Optimize campaigns by refining targeting, messaging, and channel selection.Based on the data and insights gathered, make adjustments to your marketing strategy.
Optimize campaigns by refining targeting, messaging, and channel selection.''')
    st.divider()
    st.write('10.:blue[Customer Relationship Management (CRM)]:')
    st.write('''Nurture leads and build relationships with customers through email marketing, customer support, and engagement on social media.Nurture leads and build relationships with customers through email marketing, customer support, and engagement on social media.''')
    st.divider()
    st.write('11.:blue[Feedback and Adaptation]:')
    st.write(
        '''Collect feedback from customers and clients to understand their needs and preferences.
Use this feedback to refine your products or services and adapt your marketing strategies accordingly.''')
    st.divider()
    st.write('12.:blue[Scale and Expand]:')
    st.write(
        '''As successful strategies are identified, consider scaling and expanding your marketing efforts to reach a broader audience or enter new markets.''')
    st.divider()
    st.write('13.:blue[Measure Return on Investment (ROI)]:')
    st.write(
        '''Regularly evaluate the ROI of your marketing efforts to ensure that your budget is being spent effectively.''')
    st.divider()
    st.write('14.:blue[Report and Communicate Results]:')
    st.write(
        '''Share the results and insights with relevant stakeholders within your organization to align on goals and make informed decisions.''')
    st.divider()
    st.write('15.:blue[Stay Informed and Evolve]:')
    st.write(
        '''Stay up-to-date with industry trends and changes in consumer behavior, technology, and marketing platforms.
Adapt your marketing strategies to remain relevant and effective.Stay up-to-date with industry trends and changes in consumer behavior, technology, and marketing platforms.
Adapt your marketing strategies to remain relevant and effective.''')
    st.divider()

with tab3:
    st.subheader('We provide a :green[Various] set of services,including:blue[...]')
    st.write('1.:red[Social Media Strategy]:')
    st.write(
        '''Developing a customized social media strategy that aligns with the client's goals, target audience, and brand identity.''')
    st.divider()
    st.write('2.:red[Content Creation]:')
    st.write(
        '''Creating and curating content, including posts, images, videos, infographics, and other media to engage the audience and build the brand's image.''')
    st.divider()
    st.write('3.:red[Social Media Advertising]:')
    st.write(
        '''Managing and optimizing paid advertising campaigns on platforms such as Facebook, Instagram, Twitter, LinkedIn, and others to reach a broader audience and achieve specific marketing goals.''')
    st.divider()
    st.write('4.:red[Community Management]:')
    st.write(
        '''Engaging with the audience, responding to comments and messages, and nurturing a sense of community around the brand on social media.''')
    st.divider()
    st.write('5.:red[Analytics and Reporting]:')
    st.write(
        '''Monitoring the performance of social media campaigns, tracking key metrics (e.g., reach, engagement, conversion rates), and providing regular reports to assess and improve campaign effectiveness.''')
    st.divider()
    st.write('6.:red[Influencer Marketing]:')
    st.write(
        '''Collaborating with relevant influencers to promote products or services and reach a wider audience through influencer partnerships.''')
    st.divider()
    st.write('7.:red[Social Media Listening]:')
    st.write(
        '''Monitoring and analyzing social media conversations and sentiment related to the brand, products, or industry to gain insights and adapt strategies as needed.''')
    st.divider()
    st.write('8.:red[Reputation Management]:')
    st.write(
        '''Managing and enhancing the online reputation of the brand by addressing negative reviews, comments, or public relations issues.''')
    st.divider()

with tab4:
    st.subheader('Our Team :blue[Members]')
    st.write('1.Rajiv Ranjan :red[Leader]')
    st.write('2.Surjeet')
    st.write('3.Deepanshu')
    st.write('4.Sonu')
    st.write('5.Sachin')
    st.write('6.Dharamraj')
    st.write('7.Kundan')
    st.write('8.Prince')
with tab5:
    st.subheader('Our Email')
    st.markdown('askclickwise@gmail.com')wq



