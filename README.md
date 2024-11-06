# Protect your fellow students from phishing attempts

This script is designed to help protect students at our university from phishing attacks that aim to collect their credentials.
Recently, phishing attempts targeting our university have significantly increased, with many students receiving emails prompting them to log into fake university portals designed to look like the official SOGo webmail interface.
Students who overlook the domain of these fake pages may unknowingly provide their credentials to attackers.

## How the Script works
- Fake Data Generation
    - The script generates fake usernames and uses random passwords, including entries from common password lists, to mimic real login attempts.
- Randomized User Agents
    - Each request includes a unique browser user-agent string to simulate diverse users. This makes it more challenging for attackers to filter out fake entries.
- High Volume of Requests
    - By sending many requests with random data, the script floods the attacker's database with false information, potentially making it unusable for extracting legitimate credentials.

## How to use the Script
#### Usage with Docker
- insatll docker
- Adjust the `.env.template` to fit the scammers phishing page and start the container.
- move `.env.template` to `.env`
- user `docker-compose.yml` to build and start the container


#### Usage without Docker
- install python
- create python environment
- install dependencies in `req.txt`
- run `send.py`

#### Customization
The repo comes with a `listener.py` which is a minimal server to test the `send.py` if you need to modify the script.