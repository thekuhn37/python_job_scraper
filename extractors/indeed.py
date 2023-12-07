from selenium import webdriver
from bs4 import BeautifulSoup


def get_page_count(keyword):
    driver = webdriver.Chrome()
    driver.get(
        f"https://kr.indeed.com/jobs?q={keyword}&l=&from=searchOnHP&vjk=89395b6ac5014113"
    )
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find("ul", class_="css-1g90gv6 eu4oa1w0")
    # while True:
    #     pass
    if pagination == None:
        return 1
    # return이 실행되면 해당 함수는 종료된다.  실행되지 않는 경우에만 다음 함수 내 코드로 넘어가게 된다.
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print(f"Found {pages} pages.")
    # range(5) : 0~4까지의 숫자가 들어간 범위를 나타내는 함수다.
    results = []
    for page in range(pages):
        driver = webdriver.Chrome()
        final_url = f"https://kr.indeed.com/jobs?q={keyword}&start={page*10}"
        driver.get(final_url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_list = soup.find("ul", class_="css-zu9cdh")
        jobs = job_list.find_all("li", recursive=False)
        # print(len(jobs))
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                # 아래 두 줄로 job 안의 h2 안의 a를 찾아내는 대신 select 신택스를 통해서 한 줄로 처리 가능
                # h2 = job.find('h2', class_='jobTitle')
                # a = h2.find('a')
                # select와 달리 select_one은 오로지 대상이 되는 엘레먼트 하나만 가져온다. (리스트 형태로 가져오는게 아님)
                # print(anchor)
                # 뷰티플숲의 특성 상 이렇게 가져온 정보는 단순히 텍스트가 아니라 딕셔너리 이기도 하다.
                name = job.find("span", class_="css-1x7z1ps eu4oa1w0")
                location = job.find("div", class_="css-t4u72d eu4oa1w0")
                title = anchor["aria-label"]
                link = anchor["href"]
                job_data = {
                    "link": f"https://kr.indeed.com/{link}",
                    "company": name.string.replace(",", " "),
                    "position": title.replace(",", " "),
                    "location": location.string.replace(",", " "),
                }
                results.append(job_data)
            # else:
            #     print("Mosaic li")
        # for result in results:
        #     print(result, "\n///////////\n/////////")
    return results
