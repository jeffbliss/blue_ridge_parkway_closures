# blue_ridge_parkway_closures

### Install and Run Instructions
```
git clone git@github.com:jeffbliss/blue_ridge_parkway_closures.git
pyenv virtualenv 3.9.15 parkway
pyenv activate parkway
pip install -r requirements.txt
python update_parkway.py
```

### Sample Output from above

```[{'crossroads': 'Crossroads',
  'mileposts': 'Parkway\nMileposts',
  'notes': 'Notes',
  'status': 'Status'},
 {'crossroads': 'Rockfish Gap (I-64) to VA Route 610 (Howardsville Turnpike)',
  'mileposts': '0.0 - 2.2',
  'status': 'Closed'},
 {'crossroads': 'VA Route 610 (Howardsville Turnpike) to VA Route 610 (Old '
                'Draft Drive)',
  'mileposts': '2.2 - 4.4',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 610 (Old Draft Drive) to VA Route 664 (Lyndhurst '
                'Drive),\n'
                'including Humpback Rocks Visitor Center',
  'mileposts': '4.4 - 13.6',
  'status': 'Closed'},
 {'crossroads': 'VA Route 664 (Lyndhurst Drive) to VA Route 814 (Love Road)',
  'mileposts': '13.6 - 16.1',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 814 (Love Road) to VA Route 56 (Tye River Road)',
  'mileposts': '16.1 - 27.1',
  'status': 'Open'},
 {'crossroads': 'VA Route 56 (Tye River Road) to VA Route 603 (Irish Creek '
                'Road)',
  'mileposts': '27.1 - 29.1',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 603 (Irish Creek Road) to US Route 60',
  'mileposts': '29.1 - 45.5',
  'status': 'Open'},
 {'crossroads': 'US Route 60 to VA Route 130 (Elon Road)',
  'mileposts': '45.5 -61.4',
  'notes': 'Ice and hazardous trees',
  'status': 'Closed'},
 {'crossroads': 'VA Route 130 (Elon Road) to VA Route 501,\n'
                'including James River Visitor Center',
  'mileposts': '61.4 - 66.3',
  'status': 'Open'},
 {'crossroads': 'VA Route 501 to Apple Orchard Parking Area',
  'mileposts': '66.3 - 76.4',
  'status': 'Closed'},
 {'crossroads': 'Apple Orchard Parking Area to VA Route 43 (Peaks Road),\n'
                'including Peaks of Otter Lodge',
  'mileposts': '76.4 - 85.9',
  'notes': '(Several trees down)\n'
           'Maintenance operations today near milepost 85.0',
  'status': 'Closed'},
 {'crossroads': 'VA Route 43 (Peaks Road) to Bearwallow Gap',
  'mileposts': '85.9 - 91.0',
  'status': 'Ungated'},
 {'crossroads': 'Bearwallow Gap to US Route 460',
  'mileposts': '91.0 - 105.8',
  'status': 'Open'},
 {'crossroads': 'US Route 460 to VA Route 24 (Washington Avenue)',
  'mileposts': '105.8 - 112.4',
  'status': 'Closed'},
 {'crossroads': 'VA Route 24 (Washington Avenue) to US Route 220',
  'mileposts': '112.4 -121.4',
  'status': 'Open'},
 {'crossroads': 'Explore Park Rd. (Roanoke River Pkwy)',
  'mileposts': '115.0',
  'status': 'Closed'},
 {'crossroads': 'Roanoke Mountain Loop',
  'mileposts': '120.3',
  'notes': 'Until Further Notice',
  'status': 'Closed'},
 {'crossroads': 'Mill Mountain Spur Road',
  'mileposts': '120.4',
  'status': 'Closed'},
 {'crossroads': 'US Route 220 to Adney Gap',
  'mileposts': '121.4 - 135.9',
  'notes': 'The Roanoke section of Parkway from U.S. 220 (milepost 121.4) to '
           'Adney Gap (milepost 135.9) which was previously open to cyclists '
           'and pedestrians is now *fully closed* to all visitors and '
           'recreation of any kind. Due to heavy equipment and contractors '
           'working in the area, a full closure is in place and enforceable '
           'under 36 CFR 1.5(f). Updated detour signage in place. Please see '
           'Detour Map for more detailed visual information.',
  'status': 'Closed'},
 {'crossroads': 'Adney Gap to Rocky Knob Maintenace Area',
  'mileposts': '135.9 - 167.2',
  'status': 'Ungated*'},
 {'crossroads': 'Rocky Knob Maintenace Area to VA Route 720 (Old Fields Rd),\n'
                'including Rocky Knob Picnic Area',
  'mileposts': '167.2 - 170.3',
  'status': 'Closed'},
 {'crossroads': 'VA Route 720 to VA Route 685 Turkey Ridge Road,\n'
                'including Mabry Mill & US Route 52',
  'mileposts': '170.3 - 198.4',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 685 Turkey Ridge Road\n'
                'to Ranger Road/Fancy Gap Maintenance Area',
  'mileposts': '198.4 - 199.0',
  'status': 'Open'},
 {'crossroads': 'Ranger Road/Fancy Gap Maintenance Area\n'
                'to Sunbelt/Autumnview Road',
  'mileposts': '199.0 - 200.1',
  'notes': 'Closed',
  'status': 'Ungated*'},
 {'crossroads': 'Sunbelt/Autumnview Road to VA Route 608 (Old Appalachian '
                'Trail)\n'
                'Includes I-77 Crossing',
  'mileposts': '200.1 - 202.1',
  'status': 'Open'},
 {'crossroads': 'VA Route 608 to Mahogany Rock (NC)',
  'mileposts': '202.1 - 234.1',
  'notes': 'From February 6, 2023 through April 1, 2023 there will be '
           'intermittent closures of the parkway from milepost 217-248 for '
           'winter 2022/2023 maintenance operations.',
  'status': 'Ungated*'}]
[{'crossroads': 'Crossroads',
  'mileposts': 'Parkway\nMileposts',
  'notes': 'Notes',
  'status': 'Status'},
 {'crossroads': 'Rockfish Gap (I-64) to VA Route 610 (Howardsville Turnpike)',
  'mileposts': '0.0 - 2.2',
  'status': 'Closed'},
 {'crossroads': 'VA Route 610 (Howardsville Turnpike) to VA Route 610 (Old '
                'Draft Drive)',
  'mileposts': '2.2 - 4.4',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 610 (Old Draft Drive) to VA Route 664 (Lyndhurst '
                'Drive),\n'
                'including Humpback Rocks Visitor Center',
  'mileposts': '4.4 - 13.6',
  'status': 'Closed'},
 {'crossroads': 'VA Route 664 (Lyndhurst Drive) to VA Route 814 (Love Road)',
  'mileposts': '13.6 - 16.1',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 814 (Love Road) to VA Route 56 (Tye River Road)',
  'mileposts': '16.1 - 27.1',
  'status': 'Open'},
 {'crossroads': 'VA Route 56 (Tye River Road) to VA Route 603 (Irish Creek '
                'Road)',
  'mileposts': '27.1 - 29.1',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 603 (Irish Creek Road) to US Route 60',
  'mileposts': '29.1 - 45.5',
  'status': 'Open'},
 {'crossroads': 'US Route 60 to VA Route 130 (Elon Road)',
  'mileposts': '45.5 -61.4',
  'notes': 'Ice and hazardous trees',
  'status': 'Closed'},
 {'crossroads': 'VA Route 130 (Elon Road) to VA Route 501,\n'
                'including James River Visitor Center',
  'mileposts': '61.4 - 66.3',
  'status': 'Open'},
 {'crossroads': 'VA Route 501 to Apple Orchard Parking Area',
  'mileposts': '66.3 - 76.4',
  'status': 'Closed'},
 {'crossroads': 'Apple Orchard Parking Area to VA Route 43 (Peaks Road),\n'
                'including Peaks of Otter Lodge',
  'mileposts': '76.4 - 85.9',
  'notes': '(Several trees down)\n'
           'Maintenance operations today near milepost 85.0',
  'status': 'Closed'},
 {'crossroads': 'VA Route 43 (Peaks Road) to Bearwallow Gap',
  'mileposts': '85.9 - 91.0',
  'status': 'Ungated'},
 {'crossroads': 'Bearwallow Gap to US Route 460',
  'mileposts': '91.0 - 105.8',
  'status': 'Open'},
 {'crossroads': 'US Route 460 to VA Route 24 (Washington Avenue)',
  'mileposts': '105.8 - 112.4',
  'status': 'Closed'},
 {'crossroads': 'VA Route 24 (Washington Avenue) to US Route 220',
  'mileposts': '112.4 -121.4',
  'status': 'Open'},
 {'crossroads': 'Explore Park Rd. (Roanoke River Pkwy)',
  'mileposts': '115.0',
  'status': 'Closed'},
 {'crossroads': 'Roanoke Mountain Loop',
  'mileposts': '120.3',
  'notes': 'Until Further Notice',
  'status': 'Closed'},
 {'crossroads': 'Mill Mountain Spur Road',
  'mileposts': '120.4',
  'status': 'Closed'},
 {'crossroads': 'US Route 220 to Adney Gap',
  'mileposts': '121.4 - 135.9',
  'notes': 'The Roanoke section of Parkway from U.S. 220 (milepost 121.4) to '
           'Adney Gap (milepost 135.9) which was previously open to cyclists '
           'and pedestrians is now *fully closed* to all visitors and '
           'recreation of any kind. Due to heavy equipment and contractors '
           'working in the area, a full closure is in place and enforceable '
           'under 36 CFR 1.5(f). Updated detour signage in place. Please see '
           'Detour Map for more detailed visual information.',
  'status': 'Closed'},
 {'crossroads': 'Adney Gap to Rocky Knob Maintenace Area',
  'mileposts': '135.9 - 167.2',
  'status': 'Ungated*'},
 {'crossroads': 'Rocky Knob Maintenace Area to VA Route 720 (Old Fields Rd),\n'
                'including Rocky Knob Picnic Area',
  'mileposts': '167.2 - 170.3',
  'status': 'Closed'},
 {'crossroads': 'VA Route 720 to VA Route 685 Turkey Ridge Road,\n'
                'including Mabry Mill & US Route 52',
  'mileposts': '170.3 - 198.4',
  'status': 'Ungated*'},
 {'crossroads': 'VA Route 685 Turkey Ridge Road\n'
                'to Ranger Road/Fancy Gap Maintenance Area',
  'mileposts': '198.4 - 199.0',
  'status': 'Open'},
 {'crossroads': 'Ranger Road/Fancy Gap Maintenance Area\n'
                'to Sunbelt/Autumnview Road',
  'mileposts': '199.0 - 200.1',
  'notes': 'Closed',
  'status': 'Ungated*'},
 {'crossroads': 'Sunbelt/Autumnview Road to VA Route 608 (Old Appalachian '
                'Trail)\n'
                'Includes I-77 Crossing',
  'mileposts': '200.1 - 202.1',
  'status': 'Open'},
 {'crossroads': 'VA Route 608 to Mahogany Rock (NC)',
  'mileposts': '202.1 - 234.1',
  'notes': 'From February 6, 2023 through April 1, 2023 there will be '
           'intermittent closures of the parkway from milepost 217-248 for '
           'winter 2022/2023 maintenance operations.',
  'status': 'Ungated*'},
 {'crossroads': 'Crossroads',
  'mileposts': 'Parkway\nMileposts',
  'notes': 'Notes',
  'status': 'Status'},
 {'crossroads': 'Mahogany Rock (NC) to Alligator Back Overlook',
  'mileposts': '234.1 - 242.3',
  'notes': 'From February 6, 2023 through April 1, 2023 there will be '
           'intermittent closures of the parkway from milepost 217-248 for '
           'winter 2022/2023 maintenance operations.',
  'status': 'Open'},
 {'crossroads': 'Air Bellows Gap Access Road',
  'mileposts': '237.1',
  'notes': 'From February 6, 2023 through April 1, 2023 there will be '
           'intermittent closures of the parkway from milepost 217-248 for '
           'winter 2022/2023 maintenance operations.',
  'status': 'Open'},
 {'crossroads': 'Alligator Back Overlook to Bamboo Gap',
  'mileposts': '242.3 - 285.5',
  'notes': 'From June 2022 through Nov 2024, a bridge repair project will '
           'require a detour and a full closure to all traffic from Milepost '
           '248.1 to 249.3. (Laurel Fork Bridge) Details and detour map. From '
           'January 2, 2023 through March 6, 2023 there will be intermittent '
           'closures of the parkway from milepost 217-248 for winter 2022/2023 '
           'maintenance operations.',
  'status': 'Ungated*'},
 {'crossroads': 'Bamboo Gap to Aho Gap',
  'mileposts': '285.5 - 288.0',
  'status': 'Open'},
 {'crossroads': 'Aho Gap to Green Hill Road',
  'mileposts': '288.0 - 290.8',
  'status': 'Ungated*'},
 {'crossroads': 'Green Hill Road to US Highway 321/221 Blowing Rock',
  'mileposts': '290.8 - 292.1',
  'status': 'Open'},
 {'crossroads': 'US Highway 321/221 Blowing Rock to Sandy Flat Gap, including '
                'Moses Cone Manor',
  'mileposts': '292.1 - 294.5',
  'status': 'Open'},
 {'crossroads': 'Sandy Flat Gap to Price Park Picnic Area',
  'mileposts': '294.6 - 296.4',
  'status': 'Open'},
 {'crossroads': 'Price Park Picnic Area to Holloway Mountain Road',
  'mileposts': '296.4 - 298.5',
  'status': 'Ungated'},
 {'crossroads': 'Holloway Mountain Road to US Highway 221 (Beacon Heights)',
  'mileposts': '298.5 - 305.1',
  'notes': 'From November 14, 2022 through April 1, 2023 there will be '
           'intermittent closures of the parkway from milepost 298.5-305 for '
           'winter 2022/2023 maintenance operations.',
  'status': 'Open'},
 {'crossroads': 'US Highway 221 to Beacon Heights Overlook',
  'mileposts': '305.1 - 305.2',
  'status': 'Ungated*'},
 {'crossroads': 'Beacon Heights Overlook to Roseboro Road',
  'mileposts': '305.2 - 307.9',
  'status': 'Open'},
 {'crossroads': 'Roseboro Road to Shuffler Road/Parkway Road',
  'mileposts': '307.9 - 314.6',
  'status': 'Ungated*'},
 {'crossroads': 'Shuffler Road/Parkway Road to US Highway 221 (Linville Falls)',
  'mileposts': '314.6 - 317.5',
  'status': 'Open'},
 {'crossroads': 'Linville Falls Spur Road',
  'mileposts': '316.5',
  'status': 'Open'},
 {'crossroads': 'US Highway 221 to Jacksontown Access Road (Bear Den CG)',
  'mileposts': '317.5 - 324.7',
  'status': 'Open'},
 {'crossroads': 'Jacksontown Access Road to NC Highway 226 (Gillespie Gap)',
  'mileposts': '324.7 - 330.9',
  'status': 'Ungated*'},
 {'crossroads': 'NC Highway 226 (Gillespie Gap) to Little Switzerland',
  'mileposts': '330.9 - 333.9',
  'notes': 'North Carolina Museum of Minerals is closed.',
  'status': 'Open'},
 {'crossroads': 'Little Switzerland to Victor Crossing',
  'mileposts': '333.9 - 342.1',
  'status': 'Open'},
 {'crossroads': 'Victor Crossing to NC Highway 80',
  'mileposts': '342.1 - 344.2',
  'status': 'Ungated*'},
 {'crossroads': 'NC Highway 80 to Mount Mitchell State Park',
  'mileposts': '344.2 - 355.3',
  'status': 'Open'},
 {'crossroads': 'Mount Mitchell State Park',
  'mileposts': '355.3',
  'notes': 'From January 30, 2023 through February 24, 2023 there will be '
           'intermittent closures of the parkway from milepost 355-365 for '
           'winter 2022/2023 maintenance operations. For updated information '
           'about Mt. Mitchell State Park please visit: Mount Mitchell State '
           'Park | NC State Parks (ncparks.gov)',
  'status': 'Open'},
 {'crossroads': 'NC Highway 128 to South of Craggy Gardens Tunnel,\n'
                'including Craggy Gardens Visitor Center',
  'mileposts': '355.3 - 364.5',
  'notes': 'From January 30, 2023 through February 24, 2023 there will be '
           'intermittent closures of the parkway from milepost 355-365 for '
           'winter 2022/2023 maintenance operations.',
  'status': 'Closed'},
 {'crossroads': 'South of Craggy Gardens Tunnel to North of Craggy Gardens '
                'Picnic Area',
  'mileposts': '364.5 - 367.6',
  'notes': 'Due to adverse weather conditions',
  'status': 'Closed'},
 {'crossroads': 'North of Craggy Gardens Picnic Area to Bull Gap (North of Elk '
                'Mountain/Ox Creek Road)',
  'mileposts': '367.6 - 375.7',
  'notes': 'Due to adverse weather conditions',
  'status': 'Closed'},
 {'crossroads': 'USFS Road 63 (Stoney Fork Access Rd)',
  'mileposts': '367.6',
  'notes': 'Until Further Notice',
  'status': 'Closed'},
 {'crossroads': 'Ox Creek/Elk Mountain Access Road',
  'mileposts': '375.7',
  'status': 'Open'},
 {'crossroads': 'Bull Gap (Elk Mountain/Ox Creek Road) to Folk Art Center',
  'mileposts': '375.7 - 381.9',
  'status': 'Open'},
 {'crossroads': 'Craven Gap Access Road (Town Mountain Road)',
  'mileposts': '377.4',
  'status': 'Open'},
 {'crossroads': 'Folk Art Center to Highway 70 (Tunnel Road)',
  'mileposts': '381.9 - 382.8',
  'status': 'Ungated*'},
 {'crossroads': 'Highway 70 (Tunnel Road) to Park Headquarters and Visitor '
                'Center',
  'mileposts': '382.8 - 384.1',
  'status': 'Open'},
 {'crossroads': 'Park Headquarters and Visitor Center to Highway 74 (I-40 Exit '
                '53A)',
  'mileposts': '384.1 - 384.7',
  'status': 'Ungated*'},
 {'crossroads': 'Highway 74 (I-40 Exit 53A) to Highway 25 (Hendersonville '
                'Road)',
  'mileposts': '384.7 - 388.8',
  'status': 'Open'},
 {'crossroads': 'Highway 25 (Hendersonville Road) to NC Route 191 (Brevard '
                'Road)',
  'mileposts': '388.8 - 393.6',
  'status': 'Open'},
 {'crossroads': 'NC Route 191 (Brevard Road) to Stoney Bald',
  'mileposts': '393.6 - 402.7',
  'status': 'Closed'},
 {'crossroads': 'USFS Road 5000 (Bent Creek Access Road)',
  'mileposts': '400.3',
  'status': 'Closed'},
 {'crossroads': 'Stoney Bald to NC Highway 151 Access Road',
  'mileposts': '402.7 - 405.5',
  'status': 'Closed'},
 {'crossroads': 'NC Highway 151 Access Road',
  'mileposts': '405.5',
  'status': 'Closed'},
 {'crossroads': 'Elk Pasture Gap to Pisgah Store',
  'mileposts': '405.5 - 408.8',
  'status': 'Open'},
 {'crossroads': 'Pisgah Store (Pisgah Campground and Inn) to US Route 276',
  'mileposts': '408.8 - 411.9',
  'status': 'Open'},
 {'crossroads': 'US Route 276 to North of Graveyard Fields Overlook',
  'mileposts': '411.9 - 418.7',
  'status': 'Open'},
 {'crossroads': 'North of Graveyard Fields Overlook to USFS Road 816 (Black '
                'Balsam)',
  'mileposts': '418.7 - 420.2',
  'status': 'Open'},
 {'crossroads': 'USFS Road 816 (Black Balsam) to Beech Gap (NC Route 215)',
  'mileposts': '420.2 - 423.2',
  'status': 'Open'},
 {'crossroads': 'Beech Gap (NC Route 215) to Balsam Gap (US Route 23/74)',
  'mileposts': '423.2 - 443.0',
  'status': 'Open'},
 {'crossroads': 'Balsam Gap (US Route 23/74) to Soco Gap (US Route 19)',
  'mileposts': '443.0 - 455.7',
  'status': 'Open'},
 {'crossroads': 'Soco Gap (US Route 19) to US Route 441 thru Great Smoky Mtns. '
                'NP',
  'mileposts': '455.7 - 469.1',
  'notes': 'The closure begins at Milepost 458 and continues until Milepost '
           '469 at US HWY 441. (Ice in tunnels)',
  'status': 'Closed'},
 {'crossroads': 'Heintooga Spur Road',
  'mileposts': '458.2',
  'status': 'Closed'},
 {'crossroads': 'US Route 441 thru Great Smoky Mountains National Park',
  'mileposts': '469.1',
  'notes': 'Please visit the Great Smoky Mountains National Park website for '
           'road status updates.',
  'status': 'See Note'}]```
