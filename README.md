# OOB Interaction and Internal Network Probing Script

This script is designed to identify Out-of-Band (OOB) interaction vulnerabilities and probe internal network addresses on a target web application. The script sends HTTP requests with custom headers to trigger DNS lookups and interact with internal network resources.

## Requirements

- Python 3
- `requests` library

You can install the required library using pip:

```sh
pip install requests


Explanation

    Interactsh URL: The URL for capturing OOB interactions. Replace your-payload with your actual Interactsh URL.
    Target URL: The URL of the target web application (your-in-scope-url).
    Headers: Custom headers designed to trigger DNS lookups and probe internal network resources.
    Probing Internal Endpoints: The script includes a list of internal endpoints to probe for additional information. The Referer header is set to these internal endpoints in the loop.

Impact

By running this script, you can:

    Confirm the presence of OOB interaction vulnerabilities.
    Discover internal IP addresses and network configurations.
    Potentially use the server as a pivot point for further testing.

Disclaimer

This script is intended for educational purposes and ethical security testing only. Unauthorized use of this script on systems you do not have explicit permission to test is illegal and unethical. Always obtain proper authorization before conducting any security testing. The author of this script is not responsible for any misuse or damage caused by this script.

Note: Use this script only in authorized environments and with permission to conduct security testing.
