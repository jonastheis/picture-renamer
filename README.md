# Picture Renamer

Simple tool that helps organizing pictures in folders. It renames pictures in the folder to their respective metadata date and time.
Optionally a time shift can be specified to settle a time difference from the metadata e.g. for pictures taken in a different time zone but camera settings not accordingly.

> Helps to make life easier if you want to merge pictures from multiple sources in one folder but want them in chronological order.
Or if you just can't stand the standard names and want a bit more structure.

<div style="text-align:center"><img src="assets/screenshot.png?raw=true" /></div>

## Setup & run
Prerequisites: Python3

```bash
git clone https://github.com/jonastheis/picture-renamer.git
cd picture-renamer

python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt

python main.py
```


## License
This project is licensed under the [Apache Software License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).

See [`LICENSE`](LICENSE) for more information.

    Copyright 2019 Jonas Theis
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
       http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
