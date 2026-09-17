"""The other injury hubs (truck, motorcycle, pedestrian, dog bites, slip and fall, workers' comp, catastrophic, wrongful death)
and their spokes. Each hub is built to the audit's template: an answer up front, the South Carolina law, the local specifics,
who handles it, and six to eight FAQs with markup."""
from .base import page, A, ext, img, p, ul, checks, steps, callout, answer, band, esc, table
from . import firm
from .local import cite, link

TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'
CAR = firm.CAR


def hub(slug, **kw):
    kw.setdefault("kind", "hub")
    kw.setdefault("priority", 0.85)
    kw.setdefault("author", "tara")
    return page(slug, **kw)


def sp(slug, hub_slug, eyebrow, **kw):
    kw.setdefault("kind", "spoke")
    kw["hub"] = hub_slug
    kw.setdefault("eyebrow", eyebrow)
    kw.setdefault("author", "tara")
    kw.setdefault("priority", 0.7)
    return page(slug, **kw)


FORM = '<h2>Free case review</h2><p>Tell us what happened. We will tell you whether you have a claim, what it may be worth, and what to do next.</p>[[form]]'

# ============================================================================= TRUCK ACCIDENTS
T = "practice-areas/truck-accidents"
hub(T, section_label="Truck accident guides", eyebrow="Truck accidents · Summerville, SC",
    title="Summerville Truck Accident Lawyer | 18-Wheeler Crash Attorneys",
    description="Hit by a tractor-trailer on I-26, Highway 78 or Highway 17-A? Summerville truck accident lawyers who move fast to preserve driver logs, black-box data and camera footage before the trucking company's team does. Free consultation.",
    h1="Summerville Truck Accident Lawyer", nav_label="Truck accidents",
    lead="A loaded tractor-trailer weighs 80,000 pounds. When one hits a car on I-26, the injuries are severe and the trucking company's investigators are on scene within hours. We move faster.",
    summary="18-wheeler and commercial truck crashes on I-26 and Highway 78. Federal rules, black-box data, and who is liable.",
    body=(
        answer("A truck accident claim is a car accident claim with more defendants, more evidence and more insurance. The driver, the trucking company, the owner of the trailer, the shipper who loaded it and the maintenance contractor can all share liability, and federal safety regulations create duties an ordinary driver does not have. The most important step is to preserve the electronic logs, the truck's event-data recorder and the camera footage before they are lost, which means sending a preservation demand in the first days.")
        + '<h2>I-26 and the freight corridor</h2>'
        + '<p>I-26 between the Port of Charleston and Columbia is one of the busiest freight routes in the Southeast, and it runs straight through Summerville, Ladson and North Charleston. Add the warehouses along Palmetto Commerce Parkway, the Volvo and Boeing plants and their suppliers, and the delivery fleets serving the subdivisions, and this area sees a steady volume of collisions with tractor-trailers, box trucks, dump trucks and construction vehicles. Highway 78, Highway 17-A and Dorchester Road carry the truck traffic that leaves the interstate.</p>'
        + '<h2>Why truck cases are different</h2>'
        + steps([
            ("Federal rules apply.", f" Interstate carriers must follow the Federal Motor Carrier Safety Regulations ({link('fmcsa', 'FMCSA')}): hours-of-service limits, electronic logging devices, drug and alcohol testing, driver qualification files, inspection and maintenance records. A violation is evidence of negligence, and the records exist."),
            ("There is more evidence, and it disappears faster.", " The truck's engine control module records speed, braking and throttle. The electronic logging device records hours. Many fleets run forward-facing and driver-facing cameras. The carrier is required to keep some records only for months, and a wrecked truck goes back into service or to salvage quickly. A preservation letter in week one changes the case."),
            ("There are more defendants.", f" The driver, the motor carrier, a separate owner of the tractor or trailer, the broker who arranged the load, the shipper who loaded it, and the maintenance company. Under South Carolina's apportionment rule ({cite('joint_liability')}), finding every responsible party matters."),
            ("There is more insurance, and a bigger opponent.", " Interstate carriers must carry at least $750,000 in liability coverage and most carry $1,000,000 or more. Their insurers send rapid-response teams to serious crashes the same day. You should have someone doing the same for you."),
        ])
        + '<h2>Crashes we handle</h2>'
        + checks(["Rear-end collisions when a truck fails to stop for slowed traffic on I-26", "Jackknife, rollover and underride crashes", "Wide-turn and blind-spot collisions on Highway 17-A and Dorchester Road", "Driver fatigue and hours-of-service violations", "Overloaded, unbalanced or unsecured cargo", "Brake, tire and maintenance failures", "Dump truck, concrete truck and construction vehicle crashes", "Delivery and box-truck collisions in Summerville neighborhoods"])
        + '<h2>What we do in the first two weeks</h2>'
        + checks([
            "Send preservation demands to the carrier, its insurer and the shipper for the ELD data, ECM download, camera footage, driver qualification file, dispatch records and post-crash drug test.",
            "Obtain the Highway Patrol's collision report and, in serious crashes, the Multidisciplinary Accident Investigation Team (MAIT) report.",
            "Photograph and, when warranted, have an expert inspect the truck and the scene before repairs.",
            "Identify every carrier, owner and insurer through the USDOT number on the door and the FMCSA registration.",
            "Handle every contact from the trucking company's adjusters and investigators so you do not have to.",
        ])
        + FORM
        + band("Hit by a truck on I-26?", "The trucking company's investigators are already working. Call before the evidence is gone.")
    ),
    faqs=[
        ("Why are truck accident cases different from car accidents?", "Trucking companies are governed by federal safety regulations and often have investigators on scene within hours. More parties can be held liable, the evidence is more technical and disappears faster, and the insurance limits are far higher, which is why experienced representation matters."),
        ("What evidence matters in a truck accident case?", "The electronic logging device (hours of service), the engine control module download (speed and braking), camera footage, dispatch and load records, the driver's qualification and training file, post-crash drug and alcohol tests, and the maintenance history. Most of it must be requested in writing quickly."),
        ("Who is responsible for a truck accident?", f"Potentially the driver, the motor carrier, the owner of the tractor or trailer, the broker, the shipper who loaded the cargo, and the maintenance contractor. {A(T + '/who-is-liable-in-a-truck-accident', 'How liability is sorted out')}."),
        ("What should I do immediately after a truck accident in South Carolina?", "Call 911, get medical care, photograph the truck (including the USDOT number and company name on the door), get the driver's name and carrier, and do not speak to the trucking company's insurer or investigators. Call a lawyer the same week so a preservation demand goes out."),
        ("How long do I have to file a truck accident lawsuit in South Carolina?", "Three years from the crash, like any injury claim. But the carrier's retention obligations for some records are measured in months, and the truck may be repaired or scrapped within weeks, so the practical deadline is far shorter."),
        ("How much insurance does a trucking company have?", "Federal rules require at least $750,000 for most interstate carriers hauling general freight, more for hazardous materials, and many carry $1,000,000 to $5,000,000 or more. Local and intrastate carriers can have less, which is one more reason to identify every defendant."),
    ],
    related=[T + "/who-is-liable-in-a-truck-accident", CAR, "practice-areas/catastrophic-injuries"])

sp(T + "/who-is-liable-in-a-truck-accident", T, "Truck accidents · Summerville, SC",
   title="Who Is Liable in a Truck Accident in South Carolina? | Driver, Carrier, Shipper",
   description="Who pays after a tractor-trailer crash: the driver, the motor carrier, the truck or trailer owner, the broker, the shipper who loaded the cargo, or the maintenance contractor. How South Carolina apportions fault among them.",
   h1="Who is liable in a truck accident in South Carolina?",
   summary="The driver, the carrier, the owner, the broker, the shipper or the mechanic. How fault is divided among them.",
   lead="In a car crash there is usually one defendant. In a truck crash there may be six, each with its own insurer, each pointing at the others.",
   body=(
       answer("In a South Carolina truck accident, liability can fall on the driver (negligent driving), the motor carrier (negligent hiring, training, supervision, or hours-of-service violations, and liability for its driver's negligence), the owner of the tractor or trailer, the freight broker that hired an unsafe carrier, the shipper that loaded or secured the cargo improperly, and the maintenance contractor responsible for brakes and tires. South Carolina apportions fault among all of them; a defendant found 50 percent or more at fault can be held responsible for the whole judgment.")
       + '<h2>The candidates</h2>'
       + table(["Party", "Typical basis for liability", "Where the evidence is"], [
           ["Driver", "Speeding, following too closely, fatigue, distraction, impairment", "Collision report, ECM download, ELD logs, phone records, post-crash tests"],
           ["Motor carrier", "Liable for its driver's negligence on the job; its own negligence in hiring, training, dispatching and enforcing hours", "Driver qualification file, training records, dispatch and load records, prior violations on the FMCSA safety record"],
           ["Tractor or trailer owner", "Negligent maintenance; leasing to an unsafe carrier", "Lease agreements, maintenance logs, inspection records"],
           ["Freight broker", "Selecting a carrier with a poor safety record", "Broker-carrier agreement, carrier's FMCSA history at the time of hiring"],
           ["Shipper or loader", "Overloading, unbalanced or unsecured cargo that shifts", "Bills of lading, weigh tickets, loading procedures"],
           ["Maintenance contractor", "Brake, tire or coupling failures", "Work orders, inspection reports, the parts themselves"],
           ["Government entity", "Road design or maintenance defect", "SCDOT records; Tort Claims Act deadlines and caps apply"],
       ])
       + '<h2>How South Carolina divides fault</h2>'
       + f'<p>The jury assigns a percentage of fault to every party, including the injured person. A defendant less than 50 percent at fault pays only its share; a defendant 50 percent or more at fault can be held responsible for the entire judgment ({cite("joint_liability")}). Insurers use this rule to shift blame onto empty-chair defendants and onto you, which is why every responsible party is identified and named early.</p>'
       + '<h2>Employee or independent contractor?</h2>'
       + '<p>Carriers often call their drivers independent contractors. Under federal leasing rules, a carrier that operates a truck under its USDOT authority is generally responsible for the driver\'s negligence regardless of the label. The name on the door matters; so do the lease, the dispatch records and who actually controlled the work.</p>'
       + '<h2>Why it matters to you</h2>'
       + '<p>Each additional defendant is an additional insurance policy. A driver\'s personal negligence might be covered by the carrier\'s $1,000,000 policy; a broker\'s negligent selection by another; the shipper\'s improper loading by another. In a catastrophic injury case, the difference between one policy and four is the difference between a settlement that runs out and one that does not.</p>'
       + callout("<b>Frost first:</b> photograph the USDOT number and carrier name on the truck door and the trailer's markings, which are often a different company. Those two numbers start the search for every defendant.")
   ),
   faqs=[
       ("Can I sue the trucking company, or only the driver?", "Both. The carrier is responsible for its driver's negligence on the job and may be independently liable for hiring, training or hours-of-service failures."),
       ("What if the truck driver was an independent contractor?", "Under federal leasing rules the motor carrier operating the truck under its authority is generally responsible anyway. The label rarely protects the carrier."),
       ("Can the company that loaded the truck be liable?", "Yes, when improperly loaded or secured cargo caused or contributed to the crash. Bills of lading and weigh tickets show who loaded what."),
       ("What is a freight broker, and why would it be liable?", "A broker matches shippers with carriers. One that hires a carrier with a known bad safety record can be liable for negligent selection, though these claims are contested and depend on the facts."),
   ],
   sources=[("S.C. Code § 15-38-15 (apportionment)", "https://www.scstatehouse.gov/code/t15c038.php", False), ("Federal Motor Carrier Safety Administration", "https://www.fmcsa.dot.gov/", False)],
   related=[T, "practice-areas/catastrophic-injuries", CAR + "/south-carolina-comparative-negligence"])

# ============================================================================= MOTORCYCLE
M = "practice-areas/motorcycle-accidents"
hub(M, section_label="Motorcycle accident guides", eyebrow="Motorcycle accidents · Summerville, SC",
    title="Summerville Motorcycle Accident Lawyer | Frost Law Group",
    description="Injured riding in Summerville? Motorcycle accident lawyers who counter the bias against riders, explain South Carolina's helmet law, and prove the driver who turned in front of you was at fault. Free consultation, no fee unless we win.",
    h1="Summerville Motorcycle Accident Lawyer", nav_label="Motorcycle accidents",
    lead="Riders deserve a fair shake, not blame. When a driver turns left in front of you on Dorchester Road or changes lanes into you on I-26, we prove what really happened.",
    summary="Left-turn and lane-change crashes, the helmet law, and the bias insurers use against riders.",
    body=(
        answer(f"A motorcyclist injured by a negligent driver in South Carolina has the same right to recover as anyone else: medical bills, lost income, pain and suffering, and the bike. Riders 21 and over are not required to wear a helmet ({cite('helmet')}), and not wearing one is not, by itself, fault. The obstacle in these cases is bias: adjusters assume the rider was speeding or weaving, and they price the claim accordingly. We answer that with evidence.")
        + '<h2>The crash almost every rider fears</h2>'
        + '<p>A car turns left across your lane at an intersection, or pulls out of a shopping-center driveway, because the driver “never saw” you. In our experience that is the majority of serious motorcycle crashes in the Summerville area: the Dorchester Road and Old Trolley Road intersection, the shopping-center entrances on North Main Street, the Bacons Bridge Road signals, Highway 17-A through Nexton, and the curves on Highway 61 and the roads toward Ridgeville where riders go on weekends. Lane-change crashes on I-26 and rear-end crashes at signals make up most of the rest.</p>'
        + '<p>“I didn\'t see him” is an admission of fault, not a defense. A driver has a duty to look before turning, and the law does not excuse a driver for failing to see a motorcycle that was there to be seen.</p>'
        + '<h2>How insurers treat riders, and how we answer</h2>'
        + checks([
            "<b>“He was speeding.”</b> Skid marks, the car's event-data recorder, crush damage and witness statements establish speed. Reconstruction is worth its cost in a serious case.",
            "<b>“He wasn't wearing a helmet.”</b> Legal for riders 21 and over. The defense may argue it worsened a head injury; it has no bearing on injuries to the legs, arms, spine or torso, and no bearing on who caused the crash.",
            "<b>“Motorcycles are dangerous.”</b> Not a legal argument. Choosing to ride is not negligence.",
            "<b>“He was lane-splitting.”</b> Lane-splitting is illegal in South Carolina, and it is also rare in the crashes we see. The evidence usually shows a rider in his lane and a driver who did not look.",
        ])
        + '<h2>Injuries and damages</h2>'
        + '<p>Road rash and burns, fractures of the legs, wrists and collarbone, spinal injuries, traumatic brain injuries, and amputations are common because the bike offers no protection. These cases often involve surgery, months of rehabilitation and permanent scarring. We work with your doctors and, when the injury is lasting, a life-care planner to document what the future will cost.</p>'
        + '<h2>Coverage</h2>'
        + f'<p>Many at-fault drivers carry the $25,000 state minimum, which does not cover a single surgery. Your own motorcycle policy\'s uninsured and underinsured motorist coverage, and often the UM/UIM coverage on the other vehicles in your household, can be stacked on top. {A(CAR + "/uninsured-motorist-accidents", "How UM and UIM coverage works")}.</p>'
        + FORM
        + band("Hurt riding in the Lowcountry?", "We will prove what the driver did, and answer the bias. Free consultation.")
    ),
    faqs=[
        ("Will not wearing a helmet hurt my claim?", f"South Carolina does not require helmets for riders 21 and older ({cite('helmet')}). The defense may argue a helmet would have reduced a head injury, and we answer that with medical evidence. It has nothing to do with who caused the crash or with injuries to the rest of your body. {A(M + '/south-carolina-motorcycle-helmet-law', 'The helmet law explained')}."),
        ("The insurer says the crash was my fault. Can I still recover?", "Yes, as long as you were not more than 50 percent at fault, reduced by your share. Adjusters routinely overstate a rider's fault; the physical evidence usually tells a different story."),
        ("What if the driver claims they never saw me?", "That is an admission. Drivers must look before turning or changing lanes, and a motorcycle in its lane with its headlight on was there to be seen."),
        ("What are the most common injuries in Summerville motorcycle accidents?", "Road rash and burns, leg and wrist fractures, collarbone and rib fractures, spinal injuries and traumatic brain injuries. Many require surgery and leave permanent scarring, which is compensable."),
        ("How long do I have to file a motorcycle accident claim in South Carolina?", "Three years from the crash, two if a government vehicle or road defect is involved. Evidence disappears far sooner."),
        ("Is lane-splitting legal in South Carolina?", "No. Riding between lanes of traffic is prohibited. Two motorcycles may share a lane side by side."),
    ],
    related=[M + "/south-carolina-motorcycle-helmet-law", CAR + "/south-carolina-comparative-negligence", CAR + "/uninsured-motorist-accidents"])

sp(M + "/south-carolina-motorcycle-helmet-law", M, "Motorcycle accidents · Summerville, SC",
   title="South Carolina Motorcycle Helmet Law | Who Must Wear One, and Your Claim",
   description="South Carolina requires helmets and eye protection only for riders and passengers under 21. What the law says, and how not wearing a helmet affects an injury claim after a crash.",
   h1="South Carolina's motorcycle helmet law, and what it means for your claim",
   summary="Only riders under 21 must wear a helmet. What that means when the insurer brings it up.",
   lead="South Carolina is one of the states that lets adult riders choose. Here is what the statute says and how insurers try to use it.",
   body=(
       answer(f"South Carolina requires a motorcycle helmet, and goggles or a face shield, only for operators and passengers under 21 ({cite('helmet')}). Riders 21 and over may ride without one. Not wearing a helmet is not negligence and does not affect who caused the crash. In an injury claim, the defense may argue that a helmet would have reduced a head injury, which is a damages argument limited to head injuries and answered with medical evidence.")
       + '<h2>What the statute requires</h2>'
       + checks([
           "Operators and passengers under 21: a helmet meeting the state's specifications, with a neck or chin strap, and either goggles, a face shield or a windscreen.",
           "Operators and passengers 21 and over: no helmet requirement.",
           "All riders: a working headlight, mirrors and other equipment rules that apply to every motorcycle.",
       ])
       + '<h2>How it comes up in a claim</h2>'
       + '<p>An adjuster reviewing a crash involving a rider without a helmet will raise it early, usually as a reason to discount the entire claim. That is not how the law works. Helmet use has nothing to do with fault for the collision. At most, the defense can argue that a specific head injury would have been less severe with a helmet, and that argument requires expert medical testimony, applies only to the head injury, and is often contradicted by the mechanism of the crash. A rider with a broken leg, a shattered wrist and a spinal fracture recovers for all of them regardless.</p>'
       + f'<p>South Carolina treats seat belts similarly: non-use is inadmissible in a civil case ({cite("seatbelt")}). The helmet statute has no such provision, so the question is handled case by case.</p>'
       + '<h2>The safety point</h2>'
       + f'<p>We represent riders, and we will say plainly that helmets prevent deaths. The {link("nhtsa", "NHTSA")} and the {link("iihs_motorcycle", "Insurance Institute for Highway Safety")} publish the data. Wear one. And if you did not and were hurt by a careless driver, you still have a claim.</p>'
       + callout("<b>Frost first:</b> if an adjuster tells you the claim is worth less because you were not wearing a helmet, do not argue with them. Call us; the argument is ours to make, with a doctor.")
   ),
   faqs=[
       ("Do you have to wear a helmet on a motorcycle in South Carolina?", "Only if you are under 21. Riders and passengers 21 and over may ride without one."),
       ("Can not wearing a helmet be used against me in a lawsuit?", "It cannot make you at fault for the crash. The defense may argue it increased a head injury, which requires medical evidence and applies only to head injuries."),
       ("Is eye protection required in South Carolina?", "For riders under 21, goggles, a face shield or a windscreen. Not required for adults, though strongly advised."),
   ],
   sources=[("S.C. Code § 56-5-3660 (helmets)", "https://www.scstatehouse.gov/code/t56c005.php", False), ("IIHS – motorcycle helmet laws", "https://www.iihs.org/topics/motorcycles", False)],
   related=[M, CAR + "/south-carolina-comparative-negligence", "practice-areas/catastrophic-injuries"])

# ============================================================================= PEDESTRIAN
P = "practice-areas/pedestrian-accidents"
hub(P, section_label="Pedestrian and bicycle accidents", eyebrow="Pedestrian accidents · Summerville, SC",
    title="Summerville Pedestrian Accident Lawyer | Hit by a Car in SC",
    description="Hit by a car while walking or cycling in Summerville, North Charleston or Charleston? South Carolina's crosswalk and due-care rules, how comparative fault applies to pedestrians, and where the insurance comes from.",
    h1="Summerville Pedestrian Accident Lawyer", nav_label="Pedestrian accidents",
    lead="A person on foot or on a bicycle has no protection at all. When a driver fails to yield on Dorchester Road, Rivers Avenue or Main Street, the injuries are severe and the driver's insurer will argue you should not have been there.",
    summary="Crosswalk rules, the driver's duty of due care, and coverage for people hit while walking or cycling.",
    body=(
        answer(f"A pedestrian or cyclist struck by a vehicle in South Carolina can recover from the driver's liability insurer, and from their own household auto policy's uninsured and underinsured motorist coverage, which follows them even on foot. Drivers must yield to pedestrians in crosswalks ({cite('crosswalk')}) and must exercise due care to avoid any pedestrian, anywhere ({cite('due_care')}). A pedestrian crossing outside a crosswalk shares fault but rarely more than half of it, and can still recover.")
        + '<h2>Where it happens</h2>'
        + '<p>Dorchester Road and Rivers Avenue in North Charleston, the retail stretches of North Main Street and Highway 17-A, the Ladson Road corridor, downtown Summerville around Hutchinson Square on event nights, the Sawmill Branch Trail crossings, and downtown Charleston\'s King Street, Meeting Street and the Crosstown. Many involve a pedestrian crossing a five-lane road at night with no crosswalk for a quarter mile in either direction, which is a road-design problem as much as a driver problem.</p>'
        + '<h2>The rules</h2>'
        + steps([
            ("In a crosswalk, marked or unmarked, the pedestrian has the right of way.", f" Drivers must slow or stop ({cite('crosswalk')}). Every intersection has an unmarked crosswalk at each corner, whether or not lines are painted."),
            ("Outside a crosswalk, the pedestrian must yield.", " But the driver's duty does not disappear."),
            ("Every driver must exercise due care.", f" To avoid colliding with any pedestrian, to sound the horn when necessary, and to take special care around children and people who are obviously confused or incapacitated ({cite('due_care')})."),
            ("Fault is a percentage.", f" A jaywalking pedestrian hit by a speeding, distracted driver may be 30 percent at fault and recover 70 percent. {A(CAR + '/south-carolina-comparative-negligence', 'The comparative negligence rule')}."),
        ])
        + '<h2>Bicycles</h2>'
        + '<p>Cyclists have the rights and duties of drivers on the road, and South Carolina requires drivers to leave a safe distance when passing and prohibits harassing cyclists. Crashes cluster on the roads without shoulders (Central Avenue, Bacons Bridge Road, Highway 61) and at driveways and intersections where a driver turns across the bike lane. The same insurance rules apply: the driver\'s liability policy first, then the cyclist\'s household UM/UIM coverage.</p>'
        + '<h2>Where the money comes from when a pedestrian is hit</h2>'
        + checks([
            "The driver's liability policy (often the $25,000 minimum, which a pedestrian injury exceeds almost immediately).",
            f"Your own auto policy's UM and UIM coverage, which follows you as a pedestrian or cyclist, and the policies of relatives you live with. {A(CAR + '/uninsured-motorist-accidents', 'How UM and UIM works')}.",
            "Hit-and-run: your UM coverage, provided the crash is reported to police promptly.",
            "A government entity, when a missing crosswalk, broken signal or dangerous design contributed, subject to the Tort Claims Act's two-year deadline and damage caps.",
        ])
        + FORM
        + band("Hit while walking or cycling?", "The driver's insurer will say you should not have been there. We will show what the driver did.")
    ),
    faqs=[
        ("Can a pedestrian recover if they were jaywalking in South Carolina?", "Usually yes. Crossing outside a crosswalk is shared fault, not a bar, and the driver's duty of due care remains. Recovery is reduced by the pedestrian's percentage of fault as long as it is not more than 50 percent."),
        ("I do not own a car. Is there any insurance for me?", "Possibly: the UM/UIM coverage of a relative you live with, and the driver's liability policy. We check every policy in the household."),
        ("What if the driver left the scene?", "Report it to police immediately. Your own UM coverage, or a resident relative's, pays for a hit-and-run when the driver is not found."),
        ("Do drivers have to stop for pedestrians at every corner?", "At crosswalks, marked or unmarked, when a pedestrian is crossing, yes. Every intersection has an unmarked crosswalk at each corner."),
        ("My child was hit near school. Who pays?", "The driver's insurer, your household UM/UIM coverage, and possibly the school district or town if a crossing guard, signal or school-zone failure contributed. A minor's settlement is approved by the court to protect the child."),
    ],
    related=[CAR + "/hit-and-run-accidents", CAR + "/uninsured-motorist-accidents", "practice-areas/catastrophic-injuries"])

# ============================================================================= DOG BITES
D = "practice-areas/dog-bites"
hub(D, section_label="Dog bite guides", eyebrow="Dog bites · Summerville, SC",
    title="Summerville Dog Bite Lawyer | SC Strict-Liability Claims",
    description="Bitten by a dog in Summerville, Goose Creek or Knightsville? South Carolina's strict-liability statute makes the owner responsible without a 'one free bite.' How homeowner's insurance pays, what a child's scarring claim involves, and the deadlines.",
    h1="Summerville Dog Bite Lawyer", nav_label="Dog bites",
    lead="South Carolina's strict-liability law is on your side: the owner is responsible the first time, not just after the dog has bitten before. We enforce it, especially for children.",
    summary="Strict liability under S.C. Code § 47-3-110, homeowner's insurance, children's scarring claims and the provocation defense.",
    body=(
        answer(f"Under South Carolina's dog-bite statute ({cite('dog_bite')}), the owner or keeper of a dog is liable for the full damages when the dog bites or attacks a person who is in a public place or lawfully on private property, without any need to prove the owner was careless or knew the dog was dangerous. The only real defenses are that the victim provoked the dog or was trespassing. The owner's homeowner's or renter's insurance usually pays, and claims for children's facial scarring are among the most significant injury claims we handle.")
        + '<h2>Strict liability, explained</h2>'
        + '<p>Many states follow a “one free bite” rule: the owner is responsible only if the dog had shown it was dangerous before. South Carolina rejected that rule by statute. If the dog bites or attacks you while you are somewhere you have a right to be, the owner, and anyone who had the dog in their care or keeping, is liable. It does not matter that the dog had never bitten anyone, that it was “friendly,” or that the owner did everything right. The statute is written that way because the victim, often a child, should not bear the cost of someone else\'s animal.</p>'
        + f'<p>The full text and its exceptions are on {A(D + "/south-carolina-dog-bite-law", "South Carolina’s dog bite law explained")}.</p>'
        + '<h2>The two defenses</h2>'
        + checks([
            "<b>Provocation.</b> The statute does not apply if the victim provoked or harassed the dog and that provocation was the proximate cause of the attack. Owners claim it in nearly every case; the facts rarely support it, especially for young children, whom courts are reluctant to find capable of legal provocation.",
            "<b>Not lawfully present.</b> A trespasser, or someone on the property to commit a crime, is not protected. A guest, a delivery driver, a meter reader, a child at a birthday party, and anyone on the sidewalk or in a park is protected.",
        ])
        + '<h2>Who pays</h2>'
        + f'<p>Almost always the owner\'s homeowner\'s or renter\'s insurance, which covers dog bites unless the policy excludes the breed or the dog. Landlords are generally not liable for a tenant\'s dog unless they had the dog in their own care. {A(D + "/does-homeowners-insurance-cover-dog-bites", "How the insurance works")}, including what happens when a neighbor or friend is the owner.</p>'
        + '<h2>Children</h2>'
        + f'<p>Most serious dog-bite victims are children, and most serious bites to children are to the face. A child\'s claim includes the emergency care and plastic surgery now, the scar revisions that may be needed as the child grows, the psychological effect (fear of dogs, nightmares, anxiety), and the permanent disfigurement itself. Settlements for minors are approved by the court and can be structured to fund future surgery. {A(D + "/child-bitten-by-a-dog", "What to do if your child was bitten")}.</p>'
        + '<h2>Where it happens</h2>'
        + '<p>Summerville subdivisions where a dog gets out of a fence, the Sawmill Branch Trail and neighborhood parks, dog parks, apartment complexes in Goose Creek and North Charleston, and the front yards of Knightsville and Ladson. Delivery drivers, mail carriers and children on bicycles are the most frequent victims. Bites should be reported to Dorchester County or Berkeley County animal control, which creates the record of the dog and its rabies status.</p>'
        + '<h2>What to do after a bite</h2>'
        + steps([
            ("Get medical care immediately.", " Dog bites carry a high infection risk and often need irrigation, antibiotics and sometimes closure by a plastic surgeon."),
            ("Identify the dog and owner.", " Name, address, and the dog's vaccination status. Photograph the dog if you safely can."),
            ("Report it to animal control.", " Dorchester County Animal Control (or the county where it happened). The report documents the attack and triggers the quarantine and rabies check."),
            ("Photograph the injuries.", " On the day, and then every few days as they heal. Scarring claims are proved with photographs."),
            ("Do not give a statement to the owner's insurer, and do not accept a quick check.", " Scar revision costs years later are the part the early check never covers."),
        ])
        + FORM
        + band("Bitten in Summerville or Goose Creek?", "The owner is responsible under South Carolina law. We will make the insurer honor it.")
    ),
    faqs=[
        ("Is the dog owner automatically liable in South Carolina?", "Under the strict-liability statute, the owner or keeper is liable if the dog bit or attacked you while you were in a public place or lawfully on private property, unless you provoked the dog. It does not matter whether the dog had ever bitten before."),
        ("Who pays for a dog bite claim?", "Usually the owner's homeowner's or renter's insurance. If there is none, the owner personally. We check for coverage before deciding how to proceed."),
        ("What if a child was bitten?", "The claim includes emergency care, plastic surgery, future scar revision, counseling and the disfigurement itself. Children are rarely found to have legally provoked a dog. Settlements are approved by the court and can be structured for future surgery."),
        ("What should I do immediately after a dog bite in South Carolina?", "Get medical care, identify the dog and owner, report the bite to county animal control, photograph the injuries, and do not give a recorded statement or accept a quick settlement."),
        ("How long do I have to file a dog bite injury claim in South Carolina?", "Three years from the bite. A child's own claim is preserved until adulthood, but the evidence is best gathered now."),
        ("Can I recover if the dog did not bite but knocked me down?", "Yes. The statute covers a dog that “bites or otherwise attacks.” Being knocked down or chased into traffic by a dog is covered."),
        ("Do you handle dog bites in Knightsville, Goose Creek and Ladson?", "Yes, and throughout Dorchester, Berkeley and Charleston counties. The statute is the same everywhere in the state."),
    ],
    related=[D + "/south-carolina-dog-bite-law", D + "/child-bitten-by-a-dog", D + "/does-homeowners-insurance-cover-dog-bites"])

sp(D + "/south-carolina-dog-bite-law", D, "Dog bites · Summerville, SC",
   title="South Carolina Dog Bite Law | Strict Liability Under § 47-3-110",
   description="What South Carolina's dog bite statute says: the owner or keeper is strictly liable when a dog bites or attacks a person lawfully present, with provocation as the main defense. No 'one free bite.' Explained with the text.",
   h1="What is South Carolina's dog bite law? Strict liability, explained",
   summary="The statute, the two exceptions, who counts as an owner or keeper, and what 'attacks' includes.",
   lead="South Carolina has one of the clearest dog-bite statutes in the country. Here is what it says and how courts apply it.",
   body=(
       answer(f"South Carolina Code § 47-3-110 makes the owner of a dog, or the person who has the dog in their care or keeping, liable for the full amount of damages when the dog bites or otherwise attacks a person who is in a public place or lawfully in a private place, including the owner's own property. The victim does not have to prove the owner was negligent or knew the dog was dangerous. The statute does not apply if the victim provoked or harassed the dog and that provocation caused the attack ({cite('dog_bite')}).")
       + '<h2>The elements, one by one</h2>'
       + steps([
           ("A dog bit or otherwise attacked a person.", " Bites, but also knock-downs, scratches from an attack, and injuries from fleeing a charging dog."),
           ("The person was in a public place or lawfully in a private place.", " Sidewalks, parks, trails and stores; the homes of friends and neighbors as a guest; the owner's property as a guest, a delivery driver, a contractor or a meter reader. A trespasser is not protected."),
           ("The defendant owned the dog or had it in their care or keeping.", " Owners, and also a dog-sitter, a relative watching the dog, a boarding kennel, or anyone who had taken charge of it. Landlords generally are not keepers of a tenant's dog."),
           ("The person did not provoke the dog.", " The statute's own exception: no liability if the victim provoked or harassed the dog and the provocation was the proximate cause of the attack. Ordinary conduct (walking past, reaching to pet, a child playing) is not provocation."),
       ])
       + '<h2>What “strict liability” means</h2>'
       + '<p>In a negligence case you must prove the defendant did something careless. Under the dog-bite statute you do not: the owner is liable because their dog attacked, full stop. The owner cannot defend by showing the dog had always been gentle, that the fence was adequate, or that they warned people. Those facts may matter to punitive damages or to a separate negligence claim, but they do not defeat liability under the statute.</p>'
       + '<h2>Damages under the statute</h2>'
       + '<p>“The full amount of damages”: medical bills, plastic surgery and future scar revision, lost wages, pain and suffering, disfigurement, and psychological harm. For a child, the claim can include the cost of surgery years from now and the effect of a facial scar on a lifetime.</p>'
       + '<h2>Related rules</h2>'
       + checks([
           "<b>Local leash and dangerous-dog ordinances.</b> Dorchester County, Berkeley County and the Town of Summerville each have animal-control ordinances. A violation supports a negligence claim alongside the statute and can lead to the dog being declared dangerous.",
           "<b>Comparative negligence.</b> Because the statute is strict liability, ordinary comparative fault plays a smaller role; provocation is the statutory defense.",
           f"<b>Statute of limitations.</b> Three years from the attack ({cite('sol_injury')}); a minor's claim is preserved until age 18.",
       ])
       + callout("<b>Frost first:</b> the owner's insurer will call the bite “provoked” if your hand was anywhere near the dog. Do not agree, do not explain, and let us handle it with the facts.")
   ),
   faqs=[
       ("Does South Carolina have a one-bite rule?", "No. The strict-liability statute makes the owner responsible for the first bite. The dog's history is irrelevant to liability."),
       ("Is a dog-sitter or relative liable if the dog bites while they have it?", "Yes. The statute covers anyone who had the dog in their care or keeping, in addition to the owner."),
       ("What counts as provoking a dog?", "Deliberately teasing, hitting or harassing the dog in a way that caused the attack. Walking past, reaching out to pet, or a small child's normal behavior is not provocation."),
       ("Is the landlord liable for a tenant's dog?", "Generally not under the statute, unless the landlord had the dog in their own care. A negligence claim against a landlord who knew of a dangerous dog and had control over the premises is sometimes possible."),
   ],
   sources=[("S.C. Code § 47-3-110 (liability for dog attacks)", "https://www.scstatehouse.gov/code/t47c003.php", False)],
   related=[D, D + "/child-bitten-by-a-dog", D + "/does-homeowners-insurance-cover-dog-bites"])

sp(D + "/child-bitten-by-a-dog", D, "Dog bites · Summerville, SC",
   title="My Child Was Bitten by a Neighbor's Dog in SC | What Parents Should Do",
   description="What to do when a child is bitten by a neighbor's or friend's dog in Summerville: medical care, animal control, the claim against the owner's homeowner's insurance, scarring and future surgery, and how a minor's settlement is protected.",
   h1="What if my child was bitten by a neighbor's dog?",
   summary="Medical care, the animal-control report, the neighbor's insurance, scar revision and how a minor's settlement is protected.",
   lead="Most serious dog-bite victims are children, and most serious bites to children are to the face. Here is what to do, and what the claim involves.",
   body=(
       answer(f"Get the child medical care right away (dog bites to the face often need a plastic surgeon), report the bite to county animal control, identify the dog and its vaccination status, and photograph the injuries as they heal. Under South Carolina's strict-liability statute ({cite('dog_bite')}) the owner is responsible, and the claim is paid by the owner's homeowner's or renter's insurance, not by your neighbor personally. A child's claim covers surgery now, scar revision later, counseling and the disfigurement itself, and any settlement is approved by the court to protect the child.")
       + '<h2>The first day</h2>'
       + steps([
           ("Medical care.", " Clean and irrigate the wound, and go to the emergency department or urgent care for anything deeper than a scrape. Ask for a plastic surgeon for facial wounds; how a bite is closed in the first hours affects the scar for life. Rabies and tetanus status will be checked."),
           ("Animal control.", " Report the bite to Dorchester County Animal Control (or the county where it happened). The dog will be quarantined and its rabies vaccination verified, and the report documents the attack."),
           ("The owner.", " Get their name, address and the dog's vaccination record. Stay civil. You do not need to discuss fault or insurance."),
           ("Photographs.", " The injury on day one, then every few days for weeks, then monthly. Scarring claims are proved with photographs over time."),
       ])
       + '<h2>“But they are our neighbors”</h2>'
       + f'<p>This is the reason many parents never make a claim, and it rests on a misunderstanding. The claim is against the owner\'s homeowner\'s or renter\'s insurance policy, which exists for exactly this purpose. Your neighbor pays nothing out of pocket in the ordinary case, and their premium is the insurer\'s business. Declining to make a claim does not spare your neighbor; it means your child bears the cost of surgery, and the insurer keeps the premium it was paid to cover it. {A(D + "/does-homeowners-insurance-cover-dog-bites", "How the insurance works")}.</p>'
       + '<h2>What a child\'s claim includes</h2>'
       + checks([
           "Emergency care and the initial closure or surgery.",
           "Plastic surgery and scar revision, often several procedures as the child grows, priced with a surgeon's opinion.",
           "Counseling for fear, nightmares and anxiety, which are common and treatable.",
           "The disfigurement itself: a permanent facial scar on a child is a significant element of damages.",
           "Parents' out-of-pocket costs and, in some cases, lost wages for caring for the child.",
       ])
       + '<h2>How a minor\'s settlement is protected</h2>'
       + '<p>A settlement for a child in South Carolina must be approved by a court, which reviews the amount and the attorney\'s fee and decides how the money is held: in a restricted account until the child turns 18, in a structured settlement that pays out over time, or in a trust that can fund surgery earlier. The court\'s involvement is a protection, not an obstacle.</p>'
       + '<h2>Provocation and children</h2>'
       + '<p>Owners nearly always say the child “provoked” the dog. South Carolina courts are reluctant to find that a young child is capable of legal provocation, and normal child behavior (running, squealing, hugging, reaching) is not provocation. The facts are gathered from witnesses, the animal-control report and, when necessary, an animal-behavior expert.</p>'
       + callout("<b>Frost first:</b> if the owner's insurer offers to pay the ER bill in exchange for a release, do not sign. The scar revision at 14 is the part that check never covers.")
   ),
   faqs=[
       ("Will my neighbor have to pay personally if I make a claim?", "In the ordinary case, no. The claim is paid by their homeowner's or renter's insurance, which is what the policy is for."),
       ("How long do we have to bring a claim for a child?", "A child's own claim is preserved until they turn 18, but the evidence, the witnesses and the photographs are best gathered now, and a parent's claim for medical expenses runs on the ordinary three-year deadline."),
       ("Can we get money for future plastic surgery?", "Yes, with a surgeon's opinion on what will be needed. A structured settlement or trust can hold the funds until the surgery is appropriate."),
       ("Who approves a child's settlement?", "A South Carolina court reviews and approves it and decides how the money is held for the child."),
   ],
   sources=[("S.C. Code § 47-3-110 (liability for dog attacks)", "https://www.scstatehouse.gov/code/t47c003.php", False), ("CDC – preventing dog bites", "https://www.cdc.gov/healthy-pets/about/dogs.html", False)],
   related=[D, D + "/south-carolina-dog-bite-law", D + "/does-homeowners-insurance-cover-dog-bites"])

sp(D + "/does-homeowners-insurance-cover-dog-bites", D, "Dog bites · Summerville, SC",
   title="Does Homeowner's Insurance Cover Dog Bites in South Carolina? | Who Pays",
   description="Usually yes. How a dog-bite claim is paid by the owner's homeowner's or renter's liability coverage in South Carolina, breed exclusions, what happens with no insurance, and why the claim does not come out of your neighbor's pocket.",
   h1="Does homeowner's insurance pay for a dog bite in South Carolina?",
   summary="Usually yes, through the owner's liability coverage. Breed exclusions, renters, landlords and no-insurance cases.",
   lead="The question behind most dog-bite calls is not whether the owner is liable. It is who actually pays.",
   body=(
       answer("In most cases, yes. The personal liability coverage in a standard South Carolina homeowner's or renter's policy pays for injuries the policyholder's dog causes to others, typically with limits of $100,000 to $500,000, and it pays whether the bite happened at home, on a walk or at the park. Some policies exclude certain breeds or a specific dog with a bite history, and some owners have no coverage; in those cases the claim is against the owner personally.")
       + '<h2>How the coverage works</h2>'
       + checks([
           "<b>Homeowner's policies</b> include personal liability coverage that applies to the policyholder and resident family members anywhere, not just at the house.",
           "<b>Renter's policies</b> include the same liability coverage. Apartment tenants in Goose Creek, North Charleston and Summerville often have it and do not know it.",
           "<b>Umbrella policies</b> add $1,000,000 or more above the homeowner's limits and matter in catastrophic bites.",
           "<b>Medical-payments coverage</b> on the owner's policy pays a small amount (often $1,000 to $5,000) for the victim's medical bills regardless of liability, quickly.",
       ])
       + '<h2>The exclusions</h2>'
       + '<p>Some insurers exclude breeds they consider high-risk (pit bull types, Rottweilers and others) or exclude a particular dog after a prior claim. Some require the owner to disclose the dog and void coverage if they did not. When an exclusion applies, the owner is personally liable, and whether a claim is worth pursuing depends on the owner\'s assets. We find out before recommending a course.</p>'
       + '<h2>Landlords and property owners</h2>'
       + '<p>A landlord\'s policy generally does not cover a tenant\'s dog, and South Carolina\'s statute puts liability on the owner or keeper, not the property owner. A landlord who kept the dog, or who knew of a dangerous dog and had control over the common areas where the attack occurred, may face a negligence claim.</p>'
       + '<h2>Why the claim does not come out of your neighbor\'s pocket</h2>'
       + f'<p>People hesitate to make a claim against a friend or neighbor. Understand what actually happens: the insurer pays, the owner pays nothing in the ordinary case, and the owner\'s premium is between them and the insurer. The policy was bought for this. Declining to claim means your child\'s scar-revision surgery is paid by you or not at all. {A(D + "/child-bitten-by-a-dog", "If your child was bitten")}.</p>'
       + '<h2>What we do</h2>'
       + '<p>Identify the owner and every applicable policy (homeowner\'s, renter\'s, umbrella, and sometimes a dog-sitter\'s or relative\'s), put the insurers on notice, document the injury and the scarring over time, obtain surgical opinions on future care, and negotiate or, when necessary, file suit under the strict-liability statute.</p>'
       + callout("<b>Frost first:</b> the owner's insurer may offer to pay the medical bills quickly. Fine, but not in exchange for a release, and not before the scarring has been evaluated.")
   ),
   faqs=[
       ("What if the dog owner has no insurance?", "The owner is personally liable under the statute. Whether to pursue the claim depends on their assets; we investigate before advising you."),
       ("Does renter's insurance cover dog bites?", "Usually yes. Standard renter's policies include personal liability coverage that applies to the tenant's dog."),
       ("Can the insurer deny the claim because of the dog's breed?", "If the policy has a breed exclusion, the insurer may deny coverage, leaving the owner personally liable. We obtain the policy to check."),
       ("Will the dog be put down if I make a claim?", "An insurance claim does not decide the dog's fate. Animal control decides on quarantine and dangerous-dog designations under county ordinance, separately from any claim."),
   ],
   sources=[("S.C. Code § 47-3-110 (liability for dog attacks)", "https://www.scstatehouse.gov/code/t47c003.php", False), ("South Carolina Department of Insurance", "https://doi.sc.gov/", False)],
   related=[D, D + "/south-carolina-dog-bite-law", D + "/child-bitten-by-a-dog"])

# ============================================================================= SLIP AND FALL
S = "practice-areas/slip-and-fall"
hub(S, section_label="Premises liability", eyebrow="Slip and fall · Summerville, SC",
    title="Summerville Slip & Fall Lawyer | Premises Liability | Frost Law Group",
    description="Hurt in a fall at a store, restaurant, apartment complex or parking lot in Summerville? What South Carolina requires you to prove against a property owner, the 'open and obvious' defense, and why the surveillance video must be requested this week.",
    h1="Summerville Slip &amp; Fall Lawyer", nav_label="Slip and fall",
    lead="When a property owner's negligence causes a fall, they must answer for it. These cases are won or lost on evidence that is overwritten within days.",
    summary="Falls at stores, restaurants, apartments and parking lots. What you must prove, and the video that must be requested now.",
    body=(
        answer("A property owner or business in South Carolina is liable for a fall when a dangerous condition it created, knew about, or should have discovered and fixed caused the injury, and the condition was not so open and obvious that a reasonable person would have avoided it. Customers and guests (invitees) are owed the highest duty of care. The claim is paid by the business's or homeowner's liability insurance. The critical evidence, surveillance video and incident reports, is routinely overwritten within days or weeks, so it must be requested immediately.")
        + '<h2>Where these injuries happen</h2>'
        + '<p>Grocery and big-box stores along Dorchester Road and North Main Street, the shopping centers at Azalea Square and Oakbrook, restaurants around Hutchinson Square and Nexton, apartment complexes in Goose Creek and North Charleston, hotel and parking lots along the I-26 corridor, and rental homes and vacation properties toward the coast. Wet floors, spilled produce, broken pavement, unmarked steps, loose handrails, poor lighting and ice on the rare winter morning are the usual causes.</p>'
        + '<h2>What South Carolina requires you to prove</h2>'
        + steps([
            ("A dangerous condition existed.", " Water on a tile floor, a broken stair, a pothole in the parking lot, a cord across a walkway."),
            ("The owner created it, knew about it, or should have known.", " The hardest element. A spill that happened thirty seconds before you fell is not the store's fault; a spill that sat for forty minutes with employees walking past is. Video, sweep logs and employee statements establish the timeline."),
            ("The condition was not open and obvious.", " The owner's favorite defense: you should have seen it. It fails where the hazard was hidden, where lighting was poor, where your attention was reasonably elsewhere (merchandise displays are designed to draw the eye), or where the owner should have anticipated harm anyway."),
            ("The fall caused your injury.", " Prompt medical care and a clear medical record."),
        ])
        + f'<p>Comparative negligence applies: if the jury finds you partly at fault for not watching where you walked, your recovery is reduced by that share, and barred above 50 percent. {A(CAR + "/south-carolina-comparative-negligence", "The 51 percent rule")}.</p>'
        + '<h2>What to do after a fall</h2>'
        + checks([
            "Report it to the manager before you leave, and ask for a copy of the incident report or at least its number. Do not sign a statement.",
            "Photograph the hazard, the surroundings, the lighting, any warning signs (or their absence), and your shoes.",
            "Get the names of employees and witnesses.",
            "Get medical care the same day.",
            "Keep the shoes and clothes you were wearing, unwashed.",
            "Call us before the video is overwritten. Many systems keep footage for 7 to 30 days.",
        ])
        + '<h2>Injuries and damages</h2>'
        + '<p>Hip and wrist fractures, knee injuries, back injuries, and head injuries from striking the floor or a fixture. Older adults are especially vulnerable, and a fall that would bruise a thirty-year-old can hospitalize a seventy-year-old. Damages include medical care, lost income, and pain and suffering; the owner\'s general liability policy pays.</p>'
        + '<h2>Related premises claims</h2>'
        + checks(["Negligent security: assaults in apartment complexes, parking lots and hotels with inadequate lighting, locks or patrols.", "Swimming pool injuries and drownings.", "Falling merchandise and collapsing fixtures.", "Dog attacks on the property (handled under the strict-liability statute; see " + A(D, "dog bites") + ")."])
        + FORM
        + band("Hurt in a fall at a store or apartment?", "The video is being overwritten. Call this week.")
    ),
    faqs=[
        ("Do I have a case if I fell in a store?", "Possibly. You must show the store created the hazard or knew or should have known about it and failed to fix it or warn you. We investigate the timeline with video, sweep logs and employee statements before answering."),
        ("What should I do after a slip and fall?", "Report it to the manager, photograph the hazard, get witness names, get medical care the same day, keep your shoes, and call a lawyer before the surveillance video is overwritten."),
        ("How long do I have to file a premises liability claim in South Carolina?", "Three years from the fall; two years if the property is owned by a city, county or state entity. The video may be gone in a week."),
        ("What evidence is most important in a slip and fall case?", "Surveillance video showing how long the hazard existed, the incident report, sweep and inspection logs, photographs, and witness statements. All must be preserved quickly."),
        ("What if I was partly at fault for the fall?", "You can still recover as long as you were not more than 50 percent at fault, reduced by your share. The owner will argue the hazard was open and obvious; the facts usually show otherwise."),
        ("Can I sue my landlord for a fall at my apartment?", "For a hazard in a common area (stairs, walkways, parking lots) the landlord controls, yes, if the landlord knew or should have known. Inside your unit, it depends on the lease and who was responsible for the condition."),
    ],
    related=[CAR + "/south-carolina-comparative-negligence", "practice-areas/catastrophic-injuries", D])

# ============================================================================= WORKERS' COMP
W = "practice-areas/workers-compensation"
hub(W, section_label="Workers' compensation", eyebrow="Workers' compensation · Summerville, SC",
    title="Summerville Workers' Compensation Lawyer | Frost Law Group",
    description="Hurt on the job in Summerville, Ladson or North Charleston? What South Carolina workers' compensation pays, the 90-day notice rule, who picks the doctor, denied claims before the Workers' Compensation Commission, and third-party claims that pay more.",
    h1="Summerville Workers' Compensation Lawyer", nav_label="Workers' compensation",
    lead="A workplace injury should not cost you your income or your health. South Carolina workers' compensation covers medical care and lost wages, but employers and insurers delay, deny and underpay. We handle denied and disputed claims, and the third-party claims that pay more.",
    summary="What SC workers' comp pays, the 90-day notice rule, denied claims, and third-party claims against someone other than your employer.",
    body=(
        answer(f"South Carolina workers' compensation pays for the medical treatment of a work injury, two-thirds of your average weekly wage while you cannot work (up to a state maximum), and compensation for permanent impairment, without any need to prove your employer was at fault. You must report the injury to your employer within 90 days ({cite('wc_notice')}) and file a claim within two years ({cite('wc_claim')}). The employer's insurer chooses the treating doctor. Disputes are decided by the South Carolina Workers' Compensation Commission. When someone other than your employer caused the injury, a driver, a contractor, a manufacturer, you can also bring a separate injury claim against them ({cite('wc_third_party')}).")
        + '<h2>Who is covered</h2>'
        + '<p>Nearly every South Carolina employer with four or more employees must carry workers\' compensation insurance. Construction workers, warehouse and distribution-center employees along Palmetto Commerce Parkway and in the Ladson and North Charleston industrial areas, manufacturing workers at the plants and their suppliers, healthcare workers, delivery drivers, restaurant and retail staff, and office employees are all covered. Independent contractors generally are not, though many workers labeled contractors are legally employees.</p>'
        + '<h2>What it pays</h2>'
        + checks([
            "<b>Medical care:</b> all reasonable and necessary treatment, with the insurer choosing the doctor. You can request a change, and disputes go to the Commission.",
            "<b>Temporary total disability:</b> two-thirds of your average weekly wage, up to the annual state maximum, while you are out of work on the doctor's orders, after a seven-day waiting period.",
            "<b>Temporary partial disability:</b> partial wage replacement if you return to light duty at lower pay.",
            "<b>Permanent partial or total disability:</b> compensation for lasting impairment, based on the body part, the impairment rating and the schedule in the statute, or on lost earning capacity.",
            "<b>Vocational rehabilitation</b> in some cases, and death benefits for the family of a worker killed on the job.",
        ])
        + '<p>Workers\' compensation does not pay for pain and suffering. That is what a third-party claim is for.</p>'
        + '<h2>The deadlines</h2>'
        + steps([
            ("Report the injury within 90 days.", f" To a supervisor, in writing if possible ({cite('wc_notice')}). Late notice is the most common reason claims are denied. Report it the same day."),
            ("File a claim within two years.", f" With the Workers' Compensation Commission ({cite('wc_claim')}). Reporting to your employer is not the same as filing a claim."),
        ])
        + '<h2>Denied and disputed claims</h2>'
        + f'<p>Insurers deny claims as “not work-related,” “pre-existing,” or “not reported,” cut off benefits when a doctor releases you too soon, and pressure you back to work. A denial is the beginning, not the end: we request a hearing before a Commissioner, gather the medical evidence and witness statements, and present the case. Decisions can be appealed to the full Commission and the courts. The {link("wcc", "South Carolina Workers’ Compensation Commission")} publishes its procedures.</p>'
        + '<h2>Third-party claims: when workers\' comp is not the whole answer</h2>'
        + f'<p>Workers\' compensation is your only claim against your employer ({cite("wc_exclusive")}). But if someone else caused the injury, you can sue them: the driver who hit you while you were making a delivery, the general contractor or another subcontractor on a construction site, the manufacturer of a defective machine, the property owner where you were working. A third-party claim pays for pain and suffering and full lost wages, and workers\' compensation is reimbursed from it under rules we negotiate. Delivery drivers, construction workers and workers injured in vehicle crashes on the job almost always have both claims.</p>'
        + '<h2>Retaliation</h2>'
        + '<p>South Carolina law prohibits an employer from firing or punishing you for filing a workers\' compensation claim. If it happens, you have a separate claim for wrongful discharge.</p>'
        + FORM
        + band("Hurt at work?", "Report it today, and call before you sign anything from the insurer.")
    ),
    faqs=[
        ("My workers' comp claim was denied. What now?", "A denial is not the end. We request a hearing before the South Carolina Workers' Compensation Commission and gather the medical evidence needed to prove the claim. Many denials are reversed."),
        ("Can I sue my employer for a work injury?", "Generally no; workers' compensation is the exclusive remedy against your employer. But you can sue a third party who caused the injury, such as another driver, another contractor or a product manufacturer, and that claim pays for pain and suffering."),
        ("Will I get fired for filing a claim?", "South Carolina law prohibits retaliation for filing a workers' compensation claim. If it happens, you have a separate wrongful-discharge claim."),
        ("Can I choose my own doctor for a workers' compensation injury in South Carolina?", "The employer's insurer chooses the authorized treating doctor. You can ask for a change and, if refused, ask the Commission. Treatment from an unauthorized doctor may not be paid, so ask before switching."),
        ("What should I do immediately after being injured at work in Summerville?", "Report it to a supervisor the same day, in writing if you can; get medical care and tell the provider it was a work injury; write down witnesses; keep copies of everything; and do not give a recorded statement to the insurer before talking to a lawyer."),
        ("How much does workers' comp pay while I am out of work?", "Two-thirds of your average weekly wage, up to the state maximum set each year, after a seven-day waiting period (which is paid retroactively if you are out more than 14 days)."),
        ("I am an independent contractor. Am I covered?", "Maybe. The label is not decisive; the Commission looks at who controlled the work. Many workers called contractors are legally employees and are covered."),
    ],
    related=[CAR + "/delivery-driver-accidents", "practice-areas/catastrophic-injuries", T])

# ============================================================================= CATASTROPHIC
C = "practice-areas/catastrophic-injuries"
hub(C, section_label="Catastrophic injuries", eyebrow="Catastrophic injuries · Summerville, SC",
    title="Catastrophic Injury Lawyer in Summerville, SC | Frost Law Group",
    description="Traumatic brain injury, spinal cord injury, amputation, severe burns: catastrophic injury lawyers in Summerville who build the life-care plan, find every insurance policy and value the decades ahead, not just today's bills.",
    h1="Catastrophic Injury Lawyer in Summerville, SC", nav_label="Catastrophic injuries",
    lead="Life-changing injuries demand a firm that thinks about your entire future. Insurers know these claims are worth the most, and they fight hardest to minimize them.",
    summary="Brain and spinal cord injuries, amputations and burns. Life-care plans, every policy, and the decades ahead.",
    body=(
        answer("A catastrophic injury claim in South Carolina is valued on the lifetime cost of the injury: future medical care and attendant care, home and vehicle modifications, lost earning capacity over a working life, and the loss of the life the person would have had. Proving that value takes a life-care planner, an economist and the treating physicians, and collecting it takes finding every policy that applies, because a single minimum-limits policy will not come close. These cases are prepared for trial from the first week, because that is the only way an insurer pays what they are worth.")
        + '<h2>Injuries we handle</h2>'
        + checks([
            "<b>Traumatic brain injuries (TBI)</b>, from concussions with lasting symptoms to severe injuries requiring lifelong care. Often under-diagnosed in the ER and under-valued by insurers because the injury is invisible.",
            "<b>Spinal cord injuries</b> and paralysis.",
            "<b>Amputations</b> and crush injuries, common in truck, motorcycle and workplace cases.",
            "<b>Severe burns</b> and disfigurement.",
            "<b>Multiple fractures, internal injuries and organ damage</b> requiring multiple surgeries.",
            "<b>Injuries to children</b>, whose claims must account for a lifetime.",
        ])
        + '<h2>How a catastrophic case is valued</h2>'
        + steps([
            ("The life-care plan.", " A certified life-care planner works with the treating physicians to list every need for the rest of the person's life: surgeries, therapy, medication, equipment, attendant care, home modifications, replacement wheelchairs and vans every few years. Each item is priced. Without this document, the insurer values the claim on the bills so far."),
            ("Lost earning capacity.", " A vocational expert and an economist project what the person would have earned over a working life, adjusted for the injury, and reduce it to present value."),
            ("Non-economic damages.", " Pain, suffering, disfigurement and the loss of enjoyment of life. South Carolina does not cap these damages in ordinary injury cases (the cap applies only to medical malpractice)."),
            ("Punitive damages", f" when the conduct was reckless, uncapped if the defendant was impaired ({cite('punitive_exceptions')})."),
        ])
        + '<h2>Finding the money</h2>'
        + f'<p>A catastrophic injury from a driver with a $25,000 policy is the hardest case in this practice, and the reason we look at everything: the driver\'s employer, the vehicle\'s owner, a bar that overserved, a trucking company and its broker, a product manufacturer, a government entity responsible for the road, and every uninsured and underinsured motorist policy in your household, stacked. {A(CAR + "/uninsured-motorist-accidents", "UM and UIM coverage")} and {A(T + "/who-is-liable-in-a-truck-accident", "multiple defendants in truck cases")}.</p>'
        + '<h2>Paying for care while the case is pending</h2>'
        + '<p>Health insurance, Medicare or Medicaid, MedPay, workers\' compensation if the injury was on the job, and providers who agree to wait for settlement. Each has reimbursement rights we manage so that the settlement is not consumed by liens. In a serious case we also help families with disability applications and the practical questions nobody else answers.</p>'
        + '<h2>Where these cases go</h2>'
        + '<p>Serious trauma from I-26 and the Lowcountry\'s highways goes to MUSC in Charleston, the region\'s Level I trauma center, or to Trident Medical Center in North Charleston. Rehabilitation often follows at Roper Rehabilitation Hospital or at facilities out of the area. We meet clients and families where they are.</p>'
        + FORM
        + band("A life-changing injury?", "The insurer's first offer will run out long before the care does. Talk to us before you respond to it.")
    ),
    faqs=[
        ("Why do I need a life-care plan?", "A life-care plan projects the full cost of future medical needs over a lifetime. Without one, insurers value the claim on the bills so far and offer a settlement that runs out long before the care does."),
        ("How long will my catastrophic injury case take?", "Longer than a routine claim, often one to three years, because the value cannot be known until the medical picture is clear and the experts have done their work. Settling early in a catastrophic case is almost always settling for too little."),
        ("Can I recover if I was partially at fault?", "Yes, as long as you were not more than 50 percent at fault, reduced by your share. In a catastrophic case even a small percentage matters, which is why the fault evidence is gathered so carefully."),
        ("How do I pay my medical bills while the case is pending?", "Health insurance, Medicare or Medicaid, MedPay on your auto policy, workers' compensation if the injury was on the job, and providers who treat under a letter of protection. We coordinate all of them and negotiate the liens at the end."),
        ("What is the statute of limitations for a catastrophic injury claim in South Carolina?", "Three years from the injury, two years against government entities. In a catastrophic case the work starts immediately regardless."),
        ("Does South Carolina cap damages in an injury case?", "Not for pain and suffering in ordinary injury cases. Caps apply to medical malpractice, to claims against government entities, and to punitive damages (with exceptions, including impaired defendants)."),
    ],
    related=[T, CAR + "/uninsured-motorist-accidents", "practice-areas/wrongful-death"])

# ============================================================================= WRONGFUL DEATH
WD = "practice-areas/wrongful-death"
hub(WD, section_label="Wrongful death", eyebrow="Wrongful death · Summerville, SC",
    title="Summerville Wrongful Death Lawyer | Frost Law Group",
    description="Lost a family member in a crash or other preventable accident in Summerville or the Lowcountry? Who can bring a South Carolina wrongful death claim, what it pays, the survival action, and how we handle these cases with care.",
    h1="Summerville Wrongful Death Lawyer", nav_label="Wrongful death",
    lead="Nothing restores your loss. Accountability and financial security for the family can follow, and we pursue both with the sensitivity these cases demand.",
    summary="Who can bring the claim, what South Carolina's statute pays, the survival action, and how it works after a fatal crash.",
    body=(
        answer(f"When a death in South Carolina is caused by another's wrongful act or neglect, the personal representative of the estate brings a wrongful death claim for the benefit of the surviving spouse and children (or, if none, the parents, or the heirs) under South Carolina's wrongful death statute ({cite('wrongful_death')}). It recovers funeral and medical expenses, the financial support the person would have provided, and the family's grief, mental shock, wounded feelings and loss of companionship. A separate survival action ({cite('survival')}) recovers for the person's own pain and suffering before death. Both must be filed within three years of the death.")
        + '<h2>How we handle these cases</h2>'
        + '<p>Families come to us in the worst week of their lives, usually after a fatal crash on I-26, Highway 17-A or a two-lane road, sometimes after a workplace death, a drowning or a fall. We handle the insurer, the estate paperwork the claim requires, and the investigation, so the family does not have to. We move at the family\'s pace on decisions and at the evidence\'s pace on preservation, because the two run on different clocks.</p>'
        + '<h2>Who brings the claim, and who benefits</h2>'
        + steps([
            ("The personal representative files.", " The estate's personal representative (executor or administrator) is the only person who can bring the claim, so an estate must be opened. We handle that step as part of the case."),
            ("The beneficiaries receive.", " The surviving spouse and children; if none, the parents; if none, the heirs. The proceeds pass to them directly and are not estate assets subject to the deceased's debts."),
            ("The survival action goes to the estate.", " Damages for the person's own conscious pain and suffering, medical expenses and lost wages between injury and death belong to the estate and pass under the will or intestacy."),
        ])
        + '<h2>What can be recovered</h2>'
        + checks([
            "Funeral and burial expenses, and medical expenses from the injury.",
            "The financial support and services the person would have provided over their expected life.",
            "The family's mental shock and suffering, wounded feelings, grief and sorrow, loss of companionship, and loss of the deceased's experience, knowledge and judgment in managing the family's affairs.",
            "The deceased's own conscious pain and suffering before death, through the survival action.",
            f"Punitive damages for reckless conduct, uncapped when the defendant was impaired ({cite('punitive_exceptions')}).",
        ])
        + '<h2>Fatal crashes</h2>'
        + f'<p>Most of our wrongful death cases arise from vehicle collisions: {A(CAR, "car crashes")}, {A(T, "truck crashes")}, {A(M, "motorcycle crashes")}, {A(P, "pedestrians")} struck on Dorchester Road or Rivers Avenue, and {A("practice-areas/drunk-driving-accidents", "drunk drivers")}. The Highway Patrol\'s Multidisciplinary Accident Investigation Team investigates most fatal crashes and produces a detailed reconstruction, which we obtain. The criminal case against the at-fault driver, if any, runs separately, and the family has rights as victims in it.</p>'
        + '<h2>Other causes</h2>'
        + checks(["Workplace deaths (workers' compensation death benefits plus a third-party claim against anyone other than the employer).", "Drownings and premises deaths.", "Nursing home neglect.", "Defective products.", "Dog attacks on children."])
        + FORM
        + band("We are sorry for your loss.", "When you are ready, call. We will explain what a claim involves and handle everything the family should not have to.")
    ),
    faqs=[
        ("Who can file a wrongful death claim in South Carolina?", "The personal representative of the deceased's estate files it, for the benefit of the surviving spouse and children, or the parents if there are none, or the heirs. We open the estate as part of the case if one has not been opened."),
        ("How long do we have to file?", "Three years from the date of death for the wrongful death claim. Claims against government entities have a two-year deadline. Evidence should be preserved immediately."),
        ("What is the difference between wrongful death and a survival action?", f"Wrongful death compensates the family for its loss. The survival action compensates the estate for the deceased's own pain, suffering and expenses between injury and death. Both are usually brought together. {A(WD + '/south-carolina-wrongful-death-statute', 'The statute explained')}."),
        ("What damages can be recovered in a South Carolina wrongful death claim?", "Funeral and medical expenses, lost financial support and services, and the family's grief, mental shock, wounded feelings and loss of companionship, plus punitive damages for reckless conduct."),
        ("Can the family of a drunk driving victim file a wrongful death lawsuit in South Carolina?", "Yes, against the driver and potentially the bar or store that served them, with punitive damages uncapped because the driver was impaired. The criminal case does not need to conclude first."),
        ("Do wrongful death proceeds go through the estate or to creditors?", "Wrongful death proceeds pass directly to the statutory beneficiaries and are not subject to the deceased's creditors. Survival action proceeds belong to the estate."),
    ],
    related=[WD + "/south-carolina-wrongful-death-statute", "practice-areas/drunk-driving-accidents", C])

sp(WD + "/south-carolina-wrongful-death-statute", WD, "Wrongful death · Summerville, SC",
   title="South Carolina Wrongful Death Statute, Explained | § 15-51-10 and the Survival Action",
   description="What South Carolina's wrongful death statute (S.C. Code § 15-51-10 et seq.) provides: who files, who benefits, what damages are recoverable, the three-year deadline, and how the survival action under § 15-5-90 differs.",
   h1="South Carolina's wrongful death statute, explained",
   summary="Who files, who benefits, what is recoverable, the deadline, and how the survival action differs.",
   lead="Two statutes govern a death claim in South Carolina. Here is what each one does.",
   body=(
       answer(f"South Carolina's wrongful death statute ({cite('wrongful_death')}) creates a claim, brought by the personal representative of the estate, for the benefit of the spouse and children (or parents, or heirs) when a death is caused by a wrongful act, neglect or default that would have supported an injury claim had the person lived. Damages compensate the beneficiaries for their own losses. A separate survival statute ({cite('survival')}) lets the estate pursue the claim the deceased could have brought, for pain and suffering and expenses before death. Both carry a three-year limitations period from the date of death.")
       + '<h2>The wrongful death statute (§ 15-51-10 to -60)</h2>'
       + steps([
           ("The claim (§ 15-51-10).", " Whenever a death is caused by a wrongful act, neglect or default that would have entitled the person to sue had they lived, the wrongdoer is liable to an action for damages, even if the act was also a crime."),
           ("Who brings it and who benefits (§ 15-51-20).", " The action is brought by the executor or administrator of the estate for the benefit of the wife or husband and children; if none, the parents; if none, the heirs at law. The beneficiaries do not sue in their own names."),
           ("Damages (§ 15-51-40).", " The jury awards damages proportioned to the injury resulting from the death to the beneficiaries. South Carolina courts have long held this includes pecuniary loss, mental shock and suffering, wounded feelings, grief and sorrow, loss of companionship, and deprivation of the use and comfort of the deceased's society. Punitive damages are available for reckless, willful or wanton conduct."),
           ("Distribution.", " Proceeds are divided among the beneficiaries as if the deceased had died intestate and are not liable for the estate's debts."),
       ])
       + '<h2>The survival statute (§ 15-5-90)</h2>'
       + '<p>Causes of action for injuries to the person survive the death of the injured person and are pursued by the personal representative. This is the claim the deceased would have had: conscious pain and suffering between injury and death, medical expenses, lost wages, and property damage. Its proceeds belong to the estate and pass under the will or the intestacy rules, and, unlike wrongful death proceeds, can be reached by estate creditors. In an instant death with no conscious suffering the survival claim may be small; after days or weeks in intensive care it can be substantial.</p>'
       + '<h2>The deadline</h2>'
       + f'<p>Three years from the date of death for wrongful death ({cite("sol_injury", "S.C. Code § 15-3-530(6)")}). The survival claim runs three years from the injury. Claims against a government entity must be brought within two years under the Tort Claims Act, with damages capped ({cite("tort_claims_cap")}).</p>'
       + '<h2>Practical points</h2>'
       + checks([
           "An estate must be opened and a personal representative appointed before suit can be filed. We handle that step.",
           "A settlement of a wrongful death claim must be approved by the court, which also approves the allocation between the wrongful death and survival claims and among beneficiaries.",
           "The criminal case against the person responsible, if any, is separate; a conviction is strong evidence, but the civil claim does not depend on it.",
           "Comparative negligence applies: the deceased's own share of fault, if any, reduces the recovery.",
       ])
       + callout("<b>Frost first:</b> the insurer may contact the family within days with condolences and a number. Do not sign anything. The claim belongs to the estate and its beneficiaries, and it is valued on a lifetime, not a week.")
   ),
   faqs=[
       ("Who gets the money from a wrongful death settlement in South Carolina?", "The surviving spouse and children, in intestate shares; if none, the parents; if none, the heirs. The proceeds are not subject to the deceased's debts."),
       ("Can parents sue for the wrongful death of an adult child?", "Yes, if the child left no spouse or children. Parents are the next class of beneficiaries."),
       ("Can a wrongful death claim be settled without going to court?", "It can be negotiated without a lawsuit, but the settlement must be approved by the court, which reviews the amount and the distribution."),
       ("What if the person who caused the death also died?", "The claim proceeds against that person's estate and insurer."),
   ],
   sources=[("S.C. Code Title 15, Chapter 51 (wrongful death)", "https://www.scstatehouse.gov/code/t15c051.php", False), ("S.C. Code § 15-5-90 (survival of actions)", "https://www.scstatehouse.gov/code/t15c005.php", False)],
   related=[WD, "practice-areas/drunk-driving-accidents", CAR + "/south-carolina-car-accident-statute-of-limitations"])
