"""Community pages: one per town, built from verified county/court/route data plus what genuinely differs by town for an
injury claim: who writes the crash report, which hospital handles trauma, which courthouse hears the case, and the roads
where crashes cluster. Population, ZIP and landmark facts render from the verified places data."""
from .base import page, A, ext, checks, steps, callout, band, esc, table
from . import firm
from .local import PLACES, ROUTES, directions_cards, link

TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'
DEST = firm.MAP_QUERY.replace(" ", "+")
CAR = firm.CAR

COUNTY = {
    "Dorchester County": dict(courthouse="dorchester_courthouse", seat="St. George", sheriff="Dorchester County Sheriff's Office", sheriff_key="dorchester_sheriff",
                              blurb="An injury lawsuit for a crash in Dorchester County is filed in the Court of Common Pleas at the county courthouse in St. George, about 28 miles up Highway 78 from Summerville. Claims of $7,500 or less can be heard by a county magistrate. Most claims settle with the insurer before suit, but the insurer's number depends on whether it believes the case will be filed and tried there."),
    "Berkeley County": dict(courthouse="berkeley_courthouse", seat="Moncks Corner", sheriff="Berkeley County Sheriff's Office", sheriff_key=None,
                            blurb="An injury lawsuit for a crash in Berkeley County is filed in the Court of Common Pleas at the county courthouse on California Avenue in Moncks Corner. Claims of $7,500 or less can be heard by a magistrate. Berkeley County juries have a reputation among insurers that affects how claims from this county are valued."),
    "Charleston County": dict(courthouse="charleston_judicial", seat="Charleston", sheriff="Charleston County Sheriff's Office", sheriff_key=None,
                              blurb="An injury lawsuit for a crash in Charleston County is filed in the Court of Common Pleas at the Charleston County Judicial Center on Broad Street downtown. The county is its own judicial circuit, with a busier civil docket and a jury pool drawn from the whole county, from Mount Pleasant to Edisto."),
    "Colleton County": dict(courthouse="colleton_courthouse", seat="Walterboro", sheriff="Colleton County Sheriff's Office", sheriff_key=None,
                            blurb="An injury lawsuit for a crash in Colleton County is filed in the Court of Common Pleas at the county courthouse on Hampton Street in Walterboro, part of the Fourteenth Judicial Circuit. Interstate 95 crashes make up a large share of the county's serious collisions."),
}

# Per-community facts that matter to an injury claim. Police = who writes the report; hospital = where trauma goes; roads = where crashes cluster.
CITIES = [
    dict(slug="summerville", name="Summerville", county="Dorchester County", route="i26-199", label="Home base · Flowertown",
         police="Inside the town limits, the Summerville Police Department investigates crashes and writes the collision report. On I-26 and on most state highways outside the town, it is the South Carolina Highway Patrol. In the unincorporated areas it is the Dorchester County Sheriff's Office, or the Berkeley County Sheriff's Office north of the interstate. Summerville's town limits cross into Berkeley and Charleston counties, so the agency and the county are not always the ones you expect.",
         hospital="Summerville Medical Center on Midland Parkway is the closest emergency department and a Level III trauma center. Roper St. Francis Berkeley Hospital, off Highway 17-A near Nexton, serves the north side of town. Serious trauma from I-26 crashes usually goes to Trident Medical Center in North Charleston (Level II) or MUSC in Charleston (Level I).",
         roads=["I-26 between exits 194 and 205, especially the 17-A (199) and College Park Road (203) interchanges", "North Main Street and Highway 17-A through Nexton", "Dorchester Road (SC-642) from Oakbrook to Old Trolley Road", "Bacons Bridge Road and the Berlin G. Myers Parkway intersections", "Ladson Road and Central Avenue", "Old Trolley Road and Trolley Road", "Highway 78 and Orangeburg Road toward Ridgeville"],
         intro="Summerville is home. Our office is on Linwood Lane, a mile from Hutchinson Square, and Jack Frost spent years as a Summerville police officer working the collisions on these streets. Most of our clients live within the town limits or in the Dorchester County neighborhoods around it, and a growing share in the Berkeley County part of town: Nexton, Cane Bay, Carnes Crossroads and Sangaree.",
         angle=("Three counties in one town", "A Summerville address does not tell you which county you are in. The historic core and most of the south side are Dorchester County; Nexton, Cane Bay and much of the growth north of I-26 are Berkeley County; the Ladson edge is Charleston County. The county decides which sheriff's office responds outside the town limits and which courthouse hears the case. We check it on the first call."),
         dirs=["i26-199", "nexton", "knightsville"]),
    dict(slug="goose-creek", name="Goose Creek", county="Berkeley County", route="goose-creek", label="Berkeley County's largest city",
         police="Inside the city, the Goose Creek Police Department, headquartered at the Marguerite H. Brown Municipal Center on North Goose Creek Boulevard, investigates crashes and writes the report. On Highway 52, Highway 176 and the roads outside the city limits, it is the Berkeley County Sheriff's Office or the Highway Patrol. Crashes on Joint Base Charleston property are handled by base security and federal rules.",
         hospital="Roper St. Francis Berkeley Hospital, off Highway 17-A between Goose Creek and Summerville, is the closest emergency department for most of the city. Trident Medical Center in North Charleston is the nearest Level II trauma center, about fifteen minutes down Rivers Avenue or Highway 52.",
         roads=["North Goose Creek Boulevard (US-52) and its shopping-center entrances", "St. James Avenue (US-176) from Red Bank Road to the Summerville line", "Red Bank Road and Henry E. Brown Jr. Boulevard", "Crowfield Boulevard and the Crowfield Plantation entrances", "College Park Road toward I-26", "Old Mount Holly Road and Cypress Gardens Road"],
         intro="Goose Creek produces more searches for accident lawyers than any community we serve other than Summerville itself: car accidents, hit-and-runs, drunk-driving crashes, distracted-driving and uninsured-motorist claims, most of them on Highway 52 and St. James Avenue. Our office is about twenty minutes away by Highway 176 and 17-A, and we meet Goose Creek clients at home or by video when the drive is not worth it.",
         angle=("Military families and the base", "A large share of Goose Creek families are connected to Joint Base Charleston. Service members and their dependents have questions others do not: how a deployment affects a claim, how TRICARE's reimbursement rights work, what happens when the at-fault driver is a service member with out-of-state insurance, and how a claim proceeds through a PCS move. We handle those every year."),
         dirs=["goose-creek"]),
    dict(slug="ladson", name="Ladson", county="Dorchester County", route="ladson", label="Three counties, one community",
         police="Ladson is unincorporated, so there is no town police department. The Dorchester, Berkeley or Charleston County Sheriff's Office investigates depending on which county the crash was in, and the Highway Patrol handles I-26 and US-78. The North Charleston Police Department covers the parts of Ladson inside that city's limits along Ladson Road and Palmetto Commerce Parkway.",
         hospital="Trident Medical Center in North Charleston, a Level II trauma center, is the closest emergency department for most of Ladson, about ten minutes down College Park Road or Ladson Road. Summerville Medical Center is the alternative on the Dorchester County side.",
         roads=["I-26 at the College Park Road interchange (exit 203)", "US-78 from the Summerville line to North Charleston", "Ladson Road (SC-642) and its intersections with US-78 and Palmetto Commerce Parkway", "College Park Road between US-78 and I-26", "Von Ohsen Road and Royle Road", "The Exchange Park fairgrounds traffic each fall"],
         intro="Ladson sits where Dorchester, Berkeley and Charleston counties meet, at the crossroads of US-78, Ladson Road and College Park Road, with the fairgrounds, the interstate interchange and the warehouse traffic from Palmetto Commerce Parkway. It is ten minutes from our office, and it is the community where “which county?” has to be answered before anything else.",
         angle=("Which county was the crash in?", "The county line runs through neighborhoods here. A crash on Ladson Road may be in Dorchester or Charleston County depending on which side of an intersection it happened; College Park Road crosses into Berkeley County. The county decides which sheriff's office wrote the report and which courthouse hears the case. We sort it out on the first call from the report's location codes."),
         dirs=["ladson"]),
    dict(slug="north-charleston", name="North Charleston", county="Charleston County", route="north-charleston", label="South Carolina's third-largest city",
         police="The North Charleston Police Department investigates crashes inside the city and writes the report; its traffic unit handles serious and hit-and-run collisions. On I-26 and I-526 it is the Highway Patrol. The city extends into Berkeley and Dorchester counties near Ladson and along Dorchester Road, which changes the county and the courthouse but not the police agency.",
         hospital="Trident Medical Center on Medical Plaza Drive is a Level II trauma center and receives most serious crash victims from North Charleston, Ladson and Goose Creek. MUSC in downtown Charleston, the region's Level I center, takes the most critical cases.",
         roads=["I-26 from Ashley Phosphate Road to the I-526 interchange", "Rivers Avenue (US-52/78) end to end", "Dorchester Road (SC-642) from the Summerville line to the Air Force base", "Ashley Phosphate Road, Ladson Road and Otranto Road", "Remount Road and Montague Avenue", "International Boulevard and the airport and Tanger Outlets corridor", "Rivers Avenue and Dorchester Road pedestrian crossings at night"],
         intro="North Charleston is twenty minutes down I-26 and the largest city we serve, with the region's busiest crash corridors: Rivers Avenue, Dorchester Road, Ashley Phosphate Road and the interstates. Jack Frost knows the city's police department and the Charleston County courts from his years with the Sheriff's Office, and we handle North Charleston car, truck, pedestrian and rideshare crashes every month.",
         angle=("Pedestrians and the big roads", "North Charleston's five- and seven-lane arterials, long distances between crosswalks and heavy night traffic make it the community where we see the most pedestrian and cyclist injuries. Those cases turn on the driver's duty of due care and on road design, which can bring the city or SCDOT into the claim under the Tort Claims Act's shorter deadline."),
         dirs=["north-charleston"]),
    dict(slug="charleston", name="Charleston", county="Charleston County", route="charleston", label="The peninsula and beyond",
         police="The Charleston Police Department investigates crashes on the peninsula, in West Ashley, on James Island, Johns Island and Daniel Island, and writes the report. The Highway Patrol handles I-26, the Crosstown and the bridges. Charleston County Sheriff's deputies cover the unincorporated areas.",
         hospital="MUSC Health on the peninsula is the region's Level I trauma center and receives the most serious injuries from across the Lowcountry. Roper Hospital downtown and Bon Secours St. Francis in West Ashley handle most other emergencies.",
         roads=["I-26 from the Neck to the peninsula", "The Crosstown (US-17) and the Ravenel Bridge approaches", "Meeting Street, King Street and East Bay Street", "Savannah Highway (US-17) through West Ashley", "Folly Road and Maybank Highway", "Lockwood Drive and the medical district", "King Street pedestrian crossings on weekend nights"],
         intro="Charleston is forty minutes from our office and the destination for many of the Summerville-area trips that end in a crash: commuters on I-26, hospital visits to MUSC, weekends downtown. We handle Charleston car, rideshare, pedestrian and cyclist injuries, and we file in the Charleston County Court of Common Pleas on Broad Street.",
         angle=("Rideshare, tourists and the bar districts", "Downtown Charleston's crashes have their own pattern: Uber and Lyft drivers on King and Meeting, out-of-state drivers unfamiliar with the peninsula, scooters and bicycles, and impaired drivers leaving the bar districts late. Rideshare coverage rules and out-of-state insurance questions come up in Charleston cases more than anywhere else we work."),
         dirs=["charleston"]),
    dict(slug="mount-pleasant", name="Mount Pleasant", county="Charleston County", route="mount-pleasant", label="East of the Cooper",
         police="The Mount Pleasant Police Department investigates crashes inside the town and writes the report. The Highway Patrol handles I-526, the Ravenel Bridge and US-17 outside the town limits; the Charleston County Sheriff's Office covers the unincorporated areas toward Awendaw.",
         hospital="East Cooper Medical Center on Hospital Drive is the closest emergency department. Serious trauma goes across the bridge to MUSC in downtown Charleston.",
         roads=["US-17 (Johnnie Dodds Boulevard) from the Ravenel Bridge to Highway 41", "I-526 and the Wando River bridge", "Coleman Boulevard and Ben Sawyer Boulevard toward Sullivan's Island", "Long Point Road and the I-526 interchange", "Highway 41 and the Park West and Dunes West entrances", "The Isle of Palms Connector (SC-517)", "Rifle Range Road"],
         intro="Mount Pleasant is about forty minutes from Summerville by I-26 and the Ravenel Bridge, and the searches that bring people here are for car accident lawyers after crashes on Highway 17, I-526 and Coleman Boulevard. We handle Mount Pleasant claims, file in Charleston County, and meet clients east of the Cooper when that is easier.",
         angle=("Highway 17 and the beach traffic", "Mount Pleasant's crashes cluster on Highway 17 and the roads to the beaches: heavy summer traffic, out-of-town drivers, and speed on the 17 corridor north of town. Beach-season rentals also mean out-of-state insurers and rental-car policies, which change how a claim is presented."),
         dirs=["mount-pleasant"]),
    dict(slug="moncks-corner", name="Moncks Corner", county="Berkeley County", route="moncks-corner", label="Berkeley County seat",
         police="The Moncks Corner Police Department investigates crashes inside the town and writes the report. The Berkeley County Sheriff's Office, headquartered in Moncks Corner, covers the county's unincorporated areas around Lake Moultrie, Pinopolis and Cross; the Highway Patrol handles US-52, US-17-A and SC-6 outside the town.",
         hospital="Roper St. Francis Berkeley Hospital, off Highway 17-A south of town near Nexton, is the closest emergency department. Trident Medical Center in North Charleston is the nearest Level II trauma center.",
         roads=["US-52 (Highway 52) from Goose Creek through town", "US-17-A (South Live Oak Drive) toward Summerville", "SC-6 (West Main Street) and the Highway 402 intersections", "Cypress Gardens Road and Old Highway 52", "Rembert C. Dennis Boulevard", "The two-lane roads toward Cross, Bonneau and Lake Moultrie"],
         intro="Moncks Corner is the Berkeley County seat and the town where every Berkeley County injury lawsuit is filed: the courthouse and the sheriff's office are within a few blocks of each other. It is thirty minutes from our office up Highway 17-A, and we handle crashes on Highway 52, 17-A and the lake roads for residents of Moncks Corner, Pinopolis and the surrounding county.",
         angle=("Two-lane roads and long response times", "Crashes on the rural roads around Lake Moultrie and toward Cross are often single-vehicle or head-on, at speed, and far from a hospital. Longer response and transport times mean worse outcomes and larger claims, and the evidence at a rural scene (no cameras, few witnesses) has to be gathered from the vehicles and the Highway Patrol's reconstruction."),
         dirs=["moncks-corner"]),
    dict(slug="walterboro", name="Walterboro", county="Colleton County", route="walterboro", label="Colleton County seat",
         police="The Walterboro Police Department investigates crashes inside the city and writes the report. The Colleton County Sheriff's Office covers the county's rural roads, and the Highway Patrol handles I-95, US-17-A, SC-63 and SC-64.",
         hospital="Colleton Medical Center on Robertson Boulevard is the county's emergency department. Serious trauma from I-95 goes to MUSC in Charleston or to Trident Medical Center, both about an hour away.",
         roads=["I-95 at exits 53 and 57, the county's worst stretch for serious and fatal crashes", "US-17-A between Walterboro and Summerville", "Bells Highway (SC-64) and Robertson Boulevard", "Jefferies Boulevard (US-15) through town", "Sniders Highway (SC-63)", "The rural two-lane roads toward Cottageville and Ruffin"],
         intro="Walterboro is about 45 minutes from our office down Highway 17-A, and Walterboro residents find this site searching for car accident lawyers after crashes on I-95, Highway 17-A and Bells Highway. We handle Colleton County claims, file in the Court of Common Pleas in Walterboro, and meet clients in Walterboro when the drive to Summerville is not practical.",
         angle=("I-95 and the long-distance driver", "A large share of Colleton County's serious crashes involve I-95 through-traffic: tired drivers, out-of-state and commercial vehicles, and tractor-trailers. Those cases bring in out-of-state insurers, federal trucking rules and multi-state evidence, and they are investigated by the Highway Patrol's reconstruction team, whose reports we obtain."),
         dirs=["walterboro"]),
    dict(slug="west-ashley", name="West Ashley", county="Charleston County", route="west-ashley", label="City of Charleston, west of the Ashley",
         police="West Ashley is part of the City of Charleston, so the Charleston Police Department investigates crashes and writes the report. The Highway Patrol handles I-526 and the unincorporated stretches of Highway 61 and Bees Ferry Road; Charleston County Sheriff's deputies cover the county pockets.",
         hospital="Bon Secours St. Francis Hospital on Henry Tecklenburg Drive is West Ashley's emergency department. MUSC downtown, ten minutes across the Ashley River bridges, is the Level I trauma center.",
         roads=["Savannah Highway (US-17) from the Ashley River bridges to Main Road", "Sam Rittenberg Boulevard (SC-7) and the Citadel Mall area", "Ashley River Road (SC-61), including the plantation stretch toward Summerville", "Glenn McConnell Parkway and Bees Ferry Road", "The I-526 terminus and the Paul Cantrell Boulevard interchange", "Wappoo Road and Orleans Road"],
         intro="West Ashley is about 35 minutes from our office by Ashley River Road, and it is the part of Charleston closest to the Dorchester County line. We handle West Ashley car, pedestrian and cyclist injuries on Savannah Highway, Sam Rittenberg Boulevard and Highway 61, and we file in the Charleston County Court of Common Pleas.",
         angle=("Highway 61 and the commute", "Ashley River Road between West Ashley and Summerville is a narrow, tree-lined two-lane road with heavy commuter traffic and no shoulder. Head-on and run-off-road crashes there are severe, and the road's design and maintenance can bring SCDOT into the claim under the Tort Claims Act, with its two-year deadline."),
         dirs=["west-ashley"]),
]


def facts_block(c):
    pl = PLACES.get(c["slug"])
    if not pl:
        return ""
    rows = []
    rows.append(["County", esc(pl.get("county_note") or c["county"])])
    if pl.get("status"):
        rows.append(["Status", esc(pl["status"])])
    if pl.get("zips"):
        rows.append(["ZIP codes", esc(", ".join(pl["zips"]))])
    if pl.get("population"):
        rows.append(["Population (2020 census)", esc(pl["population"])])
    if pl.get("landmarks"):
        rows.append(["Landmarks", esc("; ".join(pl["landmarks"]))])
    trs = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in rows)
    return f'<h2>About {esc(c["name"])}</h2><div class="table-wrap"><table><tbody>{trs}</tbody></table></div>'


for c in CITIES:
    co = COUNTY[c["county"]]
    court_keys = [k for k in (co["courthouse"], co.get("sheriff_key")) if k]
    r = ROUTES.get(c["route"], {})
    dist = f' The drive is about {esc(r["miles"])} miles and {esc(r["minutes"])} minutes in normal traffic.' if r.get("miles") else ""
    origin = esc(c["name"] + ", SC").replace(" ", "+")
    dir_url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={DEST}"
    body = (
        f'<p>{c["intro"]}</p>'
        f'<h2>Who investigates a crash in {esc(c["name"])}</h2>'
        f'<p>{c["police"]} Whichever agency it is, ask for the report number at the scene; we obtain the collision report, the 911 audio and any body-camera or dash-camera video for every client at no cost.</p>'
        f'<h2>Where crashes happen in {esc(c["name"])}</h2>'
        '<ul class="roads">' + "".join(f"<li>{esc(x)}</li>" for x in c["roads"]) + "</ul>"
        f'<p>Where the crash happened decides which cameras may have recorded it, which agency has the report, and which county\'s court hears the case. Tell us the intersection and we can usually tell you within a day what evidence may exist.</p>'
        f'<h2>Where the injured are treated</h2>'
        f'<p>{c["hospital"]} Get evaluated the same day even if you feel fine; the first medical record is the most important document in the claim. {A(CAR + "/auto-injury-assessment-after-a-crash", "Getting evaluated after a crash")}.</p>'
        f'<h2>Where a {esc(c["name"])} injury case is heard</h2>'
        f'<p>{co["blurb"]}</p>'
        f'[[courts:{",".join(court_keys)}]]'
        f'<h2>{esc(c["angle"][0])}</h2><p>{c["angle"][1]}</p>'
        f'<h2>How we help {esc(c["name"])} residents</h2>'
        + checks([
            f'<b>{A(CAR, "Car accidents")}</b>: rear-end, intersection, interstate, {A(CAR + "/hit-and-run-accidents", "hit-and-run")}, {A(CAR + "/distracted-driving-accidents", "distracted-driving")} and {A(CAR + "/uninsured-motorist-accidents", "uninsured-motorist")} claims.',
            f'<b>{A("practice-areas/truck-accidents", "Truck")}, {A("practice-areas/motorcycle-accidents", "motorcycle")}, {A("practice-areas/pedestrian-accidents", "pedestrian")} and {A("practice-areas/rideshare-accidents", "Uber and Lyft")} crashes</b>, and crashes caused by {A("practice-areas/drunk-driving-accidents", "drunk drivers")}.',
            f'<b>{A("practice-areas/dog-bites", "Dog bites")}</b> under South Carolina\'s strict-liability statute, especially children.',
            f'<b>{A("practice-areas/slip-and-fall", "Slip and fall")}</b> and other premises injuries at stores, restaurants and apartment complexes.',
            f'<b>{A("practice-areas/workers-compensation", "Workers’ compensation")}</b> and the third-party claims that go with it.',
            f'<b>{A("practice-areas/catastrophic-injuries", "Catastrophic injuries")}</b> and {A("practice-areas/wrongful-death", "wrongful death")}, handled with the care they demand.',
        ]) +
        f'<h2>Getting to our office from {esc(c["name"])}</h2>'
        + (f'<p>{r["text"]}{dist}</p>' if r.get("text") else f'<p>We are at 128 Linwood Lane in Summerville, off the south side of town.{dist}</p>')
        + f'<p><a class="btn ghost sm" href="{dir_url}" rel="noopener" target="_blank">Directions from {esc(c["name"])} in Google Maps</a></p>'
        + f'<p>If your injuries make the drive impractical, we come to you, at home, at the hospital or at a rehabilitation facility, or meet by phone and video.</p>'
        + facts_block(c)
        + '<h2>Free case review</h2><p>Tell us what happened. We will tell you whether you have a claim, what it may be worth, and what to do next.</p>[[form]]'
        + band(f"Injured in {c['name']}? Call Frost first.", "Free consultation, no fee unless we win, and we come to you when you cannot travel.")
    )
    faqs = [
        (f"Who writes the accident report for a crash in {c['name']}?", c["police"].split(". ")[0] + "." + (" On the interstates and state highways, the Highway Patrol." if "Highway Patrol" not in c["police"].split(". ")[0] else "")),
        (f"Which court hears a car accident lawsuit from {c['name']}?", f"The {c['county']} Court of Common Pleas in {co['seat']}, for claims over $7,500; a magistrate for smaller claims. Most claims settle with the insurer before a lawsuit is filed."),
        (f"Do you meet clients in {c['name']}?", "Yes. Consultations are at our Summerville office, at your home or hospital, or by phone and video. Injury calls are answered around the clock."),
        (f"How long do I have to file an injury claim after a crash in {c['name']}?", "Three years from the crash for a claim against another driver; two years if a city, county or state vehicle or a road defect was involved. Evidence disappears much sooner, so call early."),
    ]
    title = f"{c['name']} Car Accident & Personal Injury Lawyer | Frost Law Group"
    if len(title) > 70:
        title = f"{c['name']} Car Accident & Injury Lawyer | Frost Law Group"
    desc = f"Injured in a crash in {c['name']}, SC? Who writes the report, which hospital treats trauma, which {c['county']} court hears the case, and how Frost Law Group's injury lawyers in Summerville help. Free consultation."
    if len(desc) > 160:
        desc = f"Injured in a crash in {c['name']}, SC? Who writes the report, which court hears the case, and how Frost Law Group's Summerville injury lawyers help. Free consultation."
    county_img = {"Dorchester County": "county-dorchester.jpg", "Berkeley County": "county-berkeley.jpg", "Charleston County": "county-charleston.jpg", "Colleton County": "county-colleton.jpg"}[c["county"]]
    page("areas/" + c["slug"], kind="city", county=c["county"], section_label=c["label"], hero_image=county_img, hero_caption=c["county"],
         title=title, description=desc,
         h1=f"{c['name']} Car Accident &amp; Personal Injury Lawyer", eyebrow=f"Areas we serve · {c['county']}", nav_label=c["name"],
         lead=f"Car, truck, motorcycle and pedestrian crashes, dog bites and other injuries in {c['name']}, handled by a husband-and-wife firm in Summerville. Free consultation, no fee unless we win.",
         summary=f"Who investigates, where the injured are treated, and which court hears a {c['name']} injury case.",
         body=body, faqs=faqs, related=[CAR, "practice-areas/dog-bites", "practice-areas/truck-accidents"], priority=0.6)
