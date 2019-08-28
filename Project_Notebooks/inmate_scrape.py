def priors_scrape(base_url, list_of_slugs):
    dict_list = []
    counter = 1
    for slug in list_of_slugs:
        try:
        #getting into each individual inmates slug
            sleep(1)
            res = requests.get(base_url+slug)
        except:
            print("doesn't have a match")
            continue
        soup = BeautifulSoup(res.content)

        print('')
        print(f'slug #{counter}')
        print(slug)

        counter += 1

        #getting into what i need on the site
        tbody = soup.find('tbody')
        #class cell w-6 is the two main tables for each inmate
        div = soup.find_all('div', {'class': 'cell w-6'})

        #getting the individuals name
        #try and except for this to override this issue
        try:
            header = soup.find('header', {'class': 'auxiliary'})
            name = header.find('h1').text
        except:
            name = 'No_data'


        #there are two, and they can be indexed in
        try:
            div = soup.find_all('div', {'class': 'cell w-6'})

            column_names = div[1].find_all('th')
            individual_information = div[1].find_all('td')
            more_ind_inf = div[0].find_all('td')
        except:
            individual_information = 'No_data'
            more_ind_inf = 'No_data'


        #getting into the level of the priors table
        priors_all_info = tbody.find_all('td')
        crimes = tbody.find_all('td', {'data-title': 'Crime'})
        committed_date = tbody.find_all('td', {'data-title': 'Committed On'})
        term_of_prior = tbody.find_all('td', {'data-title': 'Term'})
        sentence_begins = tbody.find_all('td', {'data-title': 'Sentence Began'})


        #creating the dictionary to make into a dataframe
        data = {}


        #creating a for loop with the length
        for num in range(0, 4):
                try:
                    data['name'] = name
                except:
                    data['name'] = 'No_data'
                try:
                    data['TDCJ_ID'] = more_ind_inf[2].text
                except:
                    data['TDCJ_ID'] = 'No_data'
                try:
                    data['pr_crime_' + str(num)] = crimes[num].text
                except:
                    data['pr_crime_' + str(num)] = 'No_data'
                try:
                    data['pr_commit_date_' + str(num)] = committed_date[num].text
                except:
                    data['pr_commit_date_' + str(num)] = 'No_data'
                try:
                    data['pr_term_' + str(num)] = term_of_prior[num].text
                except:
                    data['pr_term_' + str(num)] = 'No_data'
                try:
                    data['pr_begins_' + str(num)] = sentence_begins[num].text
                except:
                    data['pr_begins_' + str(num)] = 'No_data'

                print(f'ind prior {num} done.')


        dict_list.append(data)


        print('And another..')


        #transforming the dictionary to a dataframe
        df = pd.DataFrame(dict_list)

        #for every 500 rows added, overwrite the csv and save
        if df.shape[0] % 100 == 0:
            df.to_csv('priors.csv')



#tester scrape basic takes the things in the main table on each individual inmate's page. columns i think are important for my model are: 'proj release date'. The others can all be used on the back end to show visuals, but I do not think sould be put directly into the model. The dataframe saves to a csv every 100 rows.
def inmate_scrape_basic(base_url, list_of_slugs):
    dict_list = []

    counter = 1
    for slug in list_of_slugs:
        try:
            sleep(1)
            res = requests.get(base_url + slug)
        except:
            print('Missing prisoner link.')
            continue
        soup = BeautifulSoup(res.content)

        print(' ')
        print(f'slug # {counter}')
        print(slug)

        counter += 1

        #errors happen on soup.finds - be sure to build try, except
        tbody = soup.find('tbody')
        div = soup.find_all('div', {'class': 'cell w-6'})


        try:
            header = soup.find('header', {'class': 'auxiliary'})
            name = header.find('h1').text
        except:
            name = 'No_data'

        div = soup.find_all('div', {'class': 'cell w-6'})

        #div[1] is the section with the info I want
        #calling all of them into a list rather than a for loop
        try:
            columns_names = div[1].find_all('th')
            individual_information = div[1].find_all('td')
            more_ind_inf = div[0].find_all('td')
        except:
            print(f'Missing prisoner link at: {slug}.')
            continue


        #creating the dictionary to make into a dataframe
        data = {}
        try:
            data['name'] = name
        except:
            data['name'] = 'No_data'
        try:
            data['sex'] = individual_information[0].text
        except:
            data['sex'] = 'No_data'
        try:
            data['race'] = individual_information[2].text
        except:
            data['race'] = 'No_data'
        try:
            data['age'] = individual_information[1].text
        except:
            data['age'] = 'No_data'
        try:
            data['max_sentence'] = more_ind_inf[0].text
        except:
            data['max_sentence'] = 'No_data'
        try:
            data['prison_unit'] = more_ind_inf[3].text
        except:
            data['prison_unit'] = 'No_data'
        try:
            data['DOB'] = more_ind_inf[4].text
        except:
            data['DOB'] = 'No_data'
        try:
            data['home_county'] = more_ind_inf[5].text
        except:
            data['home_county'] = 'No_data'
        try:
            data['TDCJ_ID'] = more_ind_inf[2].text
        except:
            data['TDCJ_ID'] = 'No_data'
        try:
            data['proj_release_date'] = more_ind_inf[1].text
        except:
            data['proj_release_date'] = 'No_data'


        dict_list.append(data)


        print('And another..')


    #transforming the dictionary to a dataframe
        df = pd.DataFrame(dict_list)

    #adding onto a saved .csv every 25 rows
        if df.shape[0] % 100 == 0:
            df.to_csv('inmate_details.csv')

    #organizing the columns in the order I want
    df_final = df[['name','TDCJ_ID', 'sex', 'race', 'age',
                   'max_sentence', 'prison_unit', 'DOB', 'proj_release_date',
                   'home_county']]

    print('Done.')

    return df_final


        print('Done.')

        return df




#this function can be used for a single prison('url'), or it can be used for all prisons by being embedded in another function that takes in the list of all prison urls. that might look like:
#full_list = []
#for slug in complete_inmate_list:
#prison = inmate_href_scrape(slug, list_of_slugs)
#full_list.append(prison)
def inmate_href_scrape(url, list_of_slugs):
    dict_list = []

    for slug in list_of_slugs:
        try:
            sleep(1)
            res = requests.get(url + slug)
            soup = BeautifulSoup(res.content)

            print(' ')
            print(slug)

            tbody = soup.find('tbody')

            for row in tbody.find_all('tr'):
                name = row.find('td', {'data-title': 'Name'})

                link = name.find({'a', 'href'}).attrs

                print(link)

                dict_list.append(link)
        except:
            print('No more pages.')
            break

    df = pd.DataFrame(dict_list)
    if df.shape[0] % 100 == 0:
            df.to_csv('inmate_slugs.csv')

    #pulling out the series to make a list of slugs
    inmate_href_list = df['href']


    print('Done.')

    return inmate_href_list





#didn't actually end up needing this information, it's all on the individual pages for each inmate
def all_prisons_main_scrape(full_prison_link_list, page_number_slugs):
    dict_list = []
    num = 1
    for prison in full_prison_link_list:

        for slug in page_number_slugs:
            try:
                sleep(1)
                res = requests.get(prison + slug)
                soup = BeautifulSoup(res.content)


                call_it = prison.split('/')[-2]

                print(f"prison {call_it} is prison {num}")
                print(f'{slug[1:]}')



                tbody = soup.find('tbody')
                head = soup.find('head')
                prison_name = head.find('title').text.split(' |')[0]


                counter = 1



                for row in tbody.find_all('tr'):
                    inmates = {}
                    try:
                        inmates['name'] = row.find('td').text.strip()
                    except:
                        inmates['name'] = None
                    try:
                        inmates['age'] = row.find('td', {'data-title': 'Age'}).text
                    except:
                        inmates['age'] = None
                    try:
                        inmates['main_crime'] = row.find('td', {'data-title': 'Main Crime'}).text
                    except:
                        inmates['main_crime'] = None
                    try:
                        inmates['entered_on'] = row.find('td', {'data-title': 'Entered On'}).text
                    except:
                        inmates['entered_on'] = None
                    try:
                        inmates['term'] = row.find('td', {'data-title': 'Term'}).text
                    except:
                        inmates['term'] = None
                    try:
                        inmates['crime_location'] = row.find('td', {'data-title': 'Crime Location'}).text
                    except:
                        inmates['crime_location'] = row.find('td', {'data-title': 'Crime Location'}).text
                    try:
                        inmates['home_county'] = row.find('td', {'data-title': 'Home County'}).text
                    except:
                        inmates['home_county'] = None
                    try:
                        inmates['prison'] = prison_name
                    except:
                        inmates['prison'] = None



                    dict_list.append(inmates)


                    print(counter)
                    counter += 1

            #this breaks once the page number goes beyond what exists in the specific list
            except:
                print(f'No more pages.')
                print(' ')
                break

        num += 1

        #transforming the dictionary to a dataframe
            df = pd.DataFrame(dict_list)

        #adding onto a saved .csv every 25 rows
            if df.shape[0] % 100 == 0:
                df.to_csv('inmate_details.csv')

    return df

    print('Finished.')
