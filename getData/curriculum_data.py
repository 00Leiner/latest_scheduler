import requests

class Fetching:
    def __init__(self, url):
        self.url = url
    
    def perform_get_request(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            # Assuming the response content is JSON
            data = response.json()
            return data
        else:
            print(f"Error in GET request. Status code: {response.status_code}")
            print(response.text)
            return None

def format_data(fetched_data):
    formatted_data = []

    for curriculum in fetched_data.get('curriculums', []):
        program_info = {
            '_id': curriculum.get('_id', ''),
            'program': curriculum.get('program', ''),
            'major': curriculum.get('major', ''),
            'year': curriculum.get('year', ''),
            'semester': curriculum.get('semester', ''),
            'curriculum': []
        }

        for course in curriculum.get('curriculum', []):
            course_info = {
                'code': course.get('code', ''),
                'description': course.get('description', ''),
                'units': course.get('units', ''),
                'type': course.get('type', '')
            }

            program_info['curriculum'].append(course_info)

        formatted_data.append(program_info)

    return formatted_data

def fetch_curriculum_data(ip):
    fetch_url = f'http://{ip}:3000/Curriculums/get'
    fetching_instance = Fetching(fetch_url)
    fetched_data = fetching_instance.perform_get_request()

    if fetched_data is not None:
        formatted_data = format_data(fetched_data)
        return formatted_data
    else:
        print('Failed to fetch data.')
        return None