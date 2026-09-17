"""Blog posts: local news and community questions about crashes, injuries and insurance, answered by the attorney who
handles those cases. Tara writes; Jack reviews (his investigation background is the natural second set of eyes).
Outbound links go to official sources (statutes, SCDMV, SCDPS, NHTSA) and to the community threads where the question
is asked (Nextdoor, Reddit, nofollow). Verified URLs come from local_data.json via local.link()."""
from .base import page, A, ext, img, p, ul, checks, steps, callout, answer, band, esc, table
from . import firm
from .local import cite, link, LINKS

TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'
DATE = "2026-09-16"
CAR = firm.CAR


def src(*keys):
    out = []
    for k in keys:
        l = LINKS.get(k)
        if l:
            out.append((l["label"], l["url"], l.get("nofollow", False)))
    return out


def post(slug, **kw):
    kw.setdefault("kind", "post")
    kw.setdefault("hub", "blog")
    kw.setdefault("date", DATE)
    kw.setdefault("cta", False)
    kw.setdefault("changefreq", "yearly")
    kw.setdefault("priority", 0.5)
    kw.setdefault("author", "tara")
    kw.setdefault("reviewer", "jack")
    return page("blog/" + slug, **kw)


# ----------------------------------------------------------------------------- 1. I-26 crash report
post("i-26-crash-summerville-who-writes-the-report", hero_image="summerville-downtown.jpg", hero_caption="Summerville", category="Car accidents",
     title="Crash on I-26 Near Summerville: Who Writes the Report, and How to Get It",
     description="After a crash on I-26 near Summerville or Ladson, the Highway Patrol writes the report, not the town police. What the FR-10 is, how to get the TR-310 from the SCDMV, and why the location code decides which county's court hears your case.",
     h1="Crash on I-26 near Summerville: who writes the report, and how to get it",
     summary="The Highway Patrol, not the town, works the interstate. What the officer hands you, what you request later, and why the mile marker matters.",
     lead="Every week someone calls after a crash on I-26 and says they cannot find their report at the Summerville Police Department. That is because it is not there.",
     body=(
         '<h2>The interstate belongs to the Highway Patrol</h2>'
         f'<p>Inside the town limits, the Summerville Police Department works crashes. On I-26, and on most of the state highways outside town, it is the {link("schp", "South Carolina Highway Patrol")}. The same is true of I-95 through Colleton County and I-526 in North Charleston and Mount Pleasant. If a trooper worked your crash, your report is a Highway Patrol report and it is obtained through the {link("scdmv_reports", "SCDMV")}, not the town.</p>'
         '<h2>What you are handed at the scene</h2>'
         f'<p>The trooper gives each driver a Form FR-10, the insurance verification form. It has the report number, the other driver\'s name and insurer, and the trooper\'s name. It is not the full report; it is the proof you need to open the insurance claim and to give your own insurer. Keep it. If no officer came, South Carolina requires the driver to send a Form FR-309 to the DMV within 15 days when there is injury, death or property damage over $1,000 ({cite("report_dmv")}).</p>'
         '<h2>The full report</h2>'
         '<p>The collision report itself is Form TR-310. It records the trooper\'s narrative and diagram, the contributing factors and any citations, the location by route and mile marker, the vehicles and their insurance, the injuries, and the witnesses. It is usually available a week or two after the crash. We request it for every client, along with the 911 audio, any dash-camera and body-camera video, and, in serious crashes, the Multidisciplinary Accident Investigation Team reconstruction.</p>'
         '<h2>Why the mile marker matters</h2>'
         f'<p>I-26 through the Summerville area runs along, and back and forth across, the Dorchester and Berkeley County line, and enters Charleston County near Ladson. The county in the report\'s location code decides where a lawsuit is filed: Dorchester County in St. George, Berkeley County in Moncks Corner, Charleston County downtown. Insurers value claims differently by county. {A(CAR + "/where-crashes-happen-in-summerville", "Where crashes happen in Summerville")} covers the corridors.</p>'
         '<h2>What people ask on Nextdoor and Reddit</h2>'
         f'<p>The question shows up on {link("nextdoor_summerville", "Nextdoor for Summerville")} and in {link("reddit_charleston", "r/Charleston")} after every bad wreck: “How do I get my accident report?” and “The trooper put me at fault, what now?” The answers: request the TR-310 from the DMV (or let us), and understand that the trooper\'s contributing-factor codes are an opinion formed in twenty minutes at the roadside, not a verdict. We have had many of them corrected with video and vehicle data.</p>'
         + callout("<b>Frost first:</b> before you call the other driver's insurer with the FR-10 in your hand, call us. The report number is all they need from you; the rest of the conversation is for their benefit, not yours.")
     ),
     sources=src("schp", "scdmv_reports", "nextdoor_summerville", "reddit_charleston") + [("S.C. Code § 56-5-1270 (accident reports to the DMV)", "https://www.scstatehouse.gov/code/t56c005.php", False)],
     related=[CAR + "/what-to-do-after-a-car-accident-in-south-carolina", CAR + "/where-crashes-happen-in-summerville", "areas/ladson"],
     faqs=[("How long does it take to get a Highway Patrol accident report in South Carolina?", "Usually one to two weeks. The FR-10 you receive at the scene is immediate; the full TR-310 follows once the trooper files it."),
           ("Can the fault finding on the report be changed?", "The report itself is rarely amended, but the contributing-factor codes are an opinion, and insurers and juries decide fault on all the evidence. Video, vehicle data and witness statements regularly overcome a roadside finding.")])

# ----------------------------------------------------------------------------- 2. Dog bites in the neighborhood
post("dog-bite-summerville-neighborhood-what-parents-should-know", hero_image="dogs.jpg", hero_caption="The Frost pups, who have never bitten anyone", category="Dog bites",
     title="A Dog Bite in a Summerville Neighborhood: What Parents Should Know",
     description="The Nextdoor post is always the same: a loose dog, a child, and a neighbor who says the dog has never bitten before. What South Carolina's strict-liability law says, who pays, and what to do in the first day.",
     h1="A dog bite in a Summerville neighborhood: what parents should know",
     summary="The loose dog, the child on a bike, the neighbor who says it never bit before. What the law says, and why the claim is not against your neighbor.",
     lead="Summer in Summerville means more kids on bikes, more dogs in yards, and, every year, the same Nextdoor thread. Here is the legal answer nobody posts.",
     body=(
         '<h2>The thread</h2>'
         f'<p>Read {link("nextdoor_summerville", "Nextdoor for Summerville")} or {link("nextdoor_goose_creek", "Goose Creek")} for a month and you will see it: a dog got through a fence in a subdivision off Bacons Bridge Road or Central Avenue, a child on a bicycle was bitten, animal control came, and the comments split between “the owner should be held responsible” and “it was an accident, the dog has never bitten anyone.” Both sides are half right about the facts and wrong about the law.</p>'
         '<h2>South Carolina has no “first bite” rule</h2>'
         f'<p>Many states excuse the owner the first time. South Carolina does not. Under {cite("dog_bite")}, the owner, or whoever had the dog in their keeping, is liable for the full damages when the dog bites or attacks a person in a public place or lawfully on private property, and it does not matter whether the dog had ever bitten before. The only real defenses are that the victim provoked the dog or was trespassing. A child riding past on the street is neither. {A("practice-areas/dog-bites/south-carolina-dog-bite-law", "The statute, explained")}.</p>'
         '<h2>The claim is against the insurance, not the neighbor</h2>'
         f'<p>The reason most parents never make a claim is that they like their neighbors. Understand what actually happens: the claim is paid by the owner\'s homeowner\'s or renter\'s insurance, which exists for exactly this. In the ordinary case the neighbor pays nothing personally. Declining to claim does not spare them; it means your child\'s scar revision at fourteen is paid by you or not at all. {A("practice-areas/dog-bites/does-homeowners-insurance-cover-dog-bites", "How the insurance works")}.</p>'
         '<h2>The first day</h2>'
         + steps([
             ("Medical care, and ask for a plastic surgeon for facial wounds.", " How a bite is closed in the first hours decides the scar for life. Rabies and tetanus status will be checked."),
             ("Report it to animal control.", " Dorchester County Animal Control for most of Summerville, Berkeley County for Nexton, Cane Bay and Sangaree. The report documents the attack and the dog's vaccination status."),
             ("Photograph the injury, on day one and every few days after.", " Scarring claims are proved with photographs over time."),
             ("Get the owner's name and address, and stay civil.", " You do not need to discuss fault, and you should not discuss insurance."),
             ("Do not accept a quick check for the ER bill.", " Not in exchange for a release. The future surgery is the part it never covers."),
         ])
         + '<h2>What a child\'s claim includes</h2>'
         + f'<p>Emergency care, plastic surgery, scar revision as the child grows, counseling for the fear and nightmares that commonly follow, and the disfigurement itself. A settlement for a minor is approved by the court and can be structured to fund surgery years from now. {A("practice-areas/dog-bites/child-bitten-by-a-dog", "If your child was bitten")}.</p>'
         + f'<p>Prevention matters too; the {link("avma_dogbites", "American Veterinary Medical Association")} publishes good guidance for families and dog owners.</p>'
         + callout("<b>Frost first:</b> the owner's insurer will call and ask whether your child \"did anything\" to the dog. That is the provocation defense being built. Decline the conversation and call us.")
     ),
     sources=src("nextdoor_summerville", "nextdoor_goose_creek", "avma_dogbites", "cdc_dogbites") + [("S.C. Code § 47-3-110 (liability for dog attacks)", "https://www.scstatehouse.gov/code/t47c003.php", False)],
     related=["practice-areas/dog-bites", "practice-areas/dog-bites/child-bitten-by-a-dog", "practice-areas/dog-bites/does-homeowners-insurance-cover-dog-bites"],
     faqs=[("Does the dog have to have bitten someone before for the owner to be liable in South Carolina?", "No. South Carolina's statute imposes strict liability from the first bite, as long as the victim was lawfully present and did not provoke the dog."),
           ("Will my neighbor have to pay out of pocket?", "In the ordinary case, no. Their homeowner's or renter's liability coverage pays the claim.")])

# ----------------------------------------------------------------------------- 3. Motorcycle season and the helmet question
post("motorcycle-season-lowcountry-helmet-law-your-claim", hero_image="county-dorchester.jpg", hero_caption="Dorchester County back roads", category="Motorcycle accidents",
     title="Motorcycle Season in the Lowcountry: The Helmet Question and Your Claim",
     description="Spring and fall bring riders to Highway 61, Highway 78 and the roads toward Ridgeville, and bring the same question after every crash: does not wearing a helmet hurt my claim? What South Carolina's helmet law says, and what insurers do with it.",
     h1="Motorcycle season in the Lowcountry: the helmet question and your claim",
     summary="Riders 21 and over may ride without a helmet in South Carolina. What that means when a driver turns left in front of you.",
     lead="The first warm weekend brings riders out on Highway 61 and the two-lane roads toward Ridgeville, and the first crash brings the same phone call.",
     body=(
         '<h2>The call</h2>'
         '<p>“A car turned left in front of me at the Dorchester Road light. I went over the hood. I wasn\'t wearing a helmet. The adjuster says that\'s a problem.” We hear a version of this every season, and the answer is the same every time: the helmet has nothing to do with who caused the crash.</p>'
         '<h2>What the law says</h2>'
         f'<p>South Carolina requires helmets and eye protection only for riders and passengers under 21 ({cite("helmet")}). Adult riders may choose. A choice the legislature made legal is not negligence, and it cannot make you at fault for a driver who failed to yield. {A("practice-areas/motorcycle-accidents/south-carolina-motorcycle-helmet-law", "The helmet law explained")}.</p>'
         '<h2>What insurers do with it</h2>'
         f'<p>Two things. First, they raise it as a general discount, hoping you will accept a lower number because you feel you were partly to blame. That is not how {A(CAR + "/south-carolina-comparative-negligence", "comparative negligence")} works; fault is about causing the crash. Second, in a case with a head injury, they may argue a helmet would have reduced it. That is a damages argument, it applies only to the head injury, it requires a doctor\'s testimony, and it has no effect on the broken leg, the road rash or the shattered wrist. We answer it with medical evidence, and often the mechanism of the crash answers it for us.</p>'
         '<h2>The crash that actually happens</h2>'
         '<p>Left turns across the rider\'s lane at the Dorchester Road and Old Trolley Road intersection, the shopping-center entrances on North Main Street, Bacons Bridge Road and Highway 17-A through Nexton. The driver “never saw” the motorcycle. That is an admission, not a defense: drivers must look before turning, and a motorcycle in its lane with its headlight on was there to be seen. Lane-change crashes on I-26 and rear-end crashes at signals make up most of the rest.</p>'
         '<h2>The safety point, plainly</h2>'
         f'<p>We represent riders, and we will say it: helmets prevent deaths. The {link("nhtsa", "NHTSA")} and the {link("iihs_motorcycle", "Insurance Institute for Highway Safety")} publish the numbers. Wear one. And if you did not, and a careless driver hurt you, you still have a claim.</p>'
         + callout("<b>Frost first:</b> if an adjuster says the claim is worth less because of the helmet, do not argue with them. The argument is ours to make, with a doctor.")
     ),
     sources=src("nhtsa", "iihs_motorcycle", "reddit_charleston") + [("S.C. Code § 56-5-3660 (helmets)", "https://www.scstatehouse.gov/code/t56c005.php", False)],
     related=["practice-areas/motorcycle-accidents", "practice-areas/motorcycle-accidents/south-carolina-motorcycle-helmet-law", CAR + "/south-carolina-comparative-negligence"],
     faqs=[("Can the insurance company reduce my claim because I was not wearing a helmet?", "Not for fault. At most, in a case with a head injury, the defense can argue with medical evidence that a helmet would have reduced that injury."),
           ("Is lane-splitting legal in South Carolina?", "No. Riding between lanes is prohibited; two motorcycles may share a lane side by side.")])

# ----------------------------------------------------------------------------- 4. Goose Creek UM
post("hit-by-an-uninsured-driver-goose-creek-your-own-policy", hero_image="county-berkeley.jpg", hero_caption="Berkeley County", category="Car accidents",
     title="Hit by an Uninsured Driver in Goose Creek? Your Own Policy Is the Answer",
     description="Goose Creek residents search for uninsured-motorist accident lawyers more than any community we serve. How South Carolina's mandatory UM coverage and optional UIM coverage pay when the driver who hit you on Highway 52 had nothing, and the mistakes that forfeit it.",
     h1="Hit by an uninsured driver in Goose Creek? Your own policy is the answer",
     summary="Why so many Goose Creek crashes involve uninsured drivers, and how your UM and UIM coverage pays when theirs does not.",
     lead="The other driver's insurance card was expired, or fake, or the policy was cancelled last month. On Highway 52 that is not rare. Here is where the money actually comes from.",
     body=(
         '<h2>Why it happens so often here</h2>'
         f'<p>Search data shows Goose Creek residents looking for uninsured-motorist accident lawyers more than any other community we serve, and it matches what we see: minimum-limits policies cancelled for non-payment, drivers with no coverage at all, and hit-and-runs on North Goose Creek Boulevard and St. James Avenue. Roughly one South Carolina driver in ten has no insurance, and the state minimum for those who do is $25,000 ({cite("min_liability")}), which does not cover a single surgery.</p>'
         '<h2>The coverage you already have</h2>'
         + steps([
             ("Uninsured motorist (UM).", f" Required on every South Carolina policy ({cite('um')}). It pays your claim when the at-fault driver has no insurance, cannot be identified, or was in a stolen car, up to your UM limits."),
             ("Underinsured motorist (UIM).", f" Must be offered to you ({cite('uim')}). It pays when the at-fault driver's limits are less than your damages. If the offer was not made properly, courts have read the coverage into the policy anyway; we check the form."),
             ("Stacking.", " If your household has more than one vehicle, or you were in someone else's car, the limits of each policy may add together. A $25,000 case becomes a $100,000 case."),
         ])
         + f'<p>The full explanation, including the hit-and-run witness rule and the settlement-consent trap, is on {A(CAR + "/uninsured-motorist-accidents", "uninsured and underinsured motorist claims")}.</p>'
         '<h2>The mistakes that forfeit it</h2>'
         + checks([
             "Settling with the at-fault driver's minimum-limits insurer without your own UIM carrier's written consent. Your policy requires it; sign without it and the UIM claim can be lost.",
             "Not reporting a hit-and-run to police promptly. The UM statute requires it.",
             "Giving your own insurer a recorded statement that understates the injury. On a UM claim, your own company defends the claim the way the other side would.",
         ])
         + '<h2>Goose Creek specifics</h2>'
         + f'<p>Crashes inside the city are investigated by the Goose Creek Police Department; on Highway 52 and 176 outside the limits, by the Berkeley County Sheriff\'s Office or the Highway Patrol. Lawsuits are filed in the Berkeley County Court of Common Pleas in Moncks Corner. Military families at Joint Base Charleston have added questions about TRICARE reimbursement and out-of-state policies that we handle every year. {A("areas/goose-creek", "Our Goose Creek page")} covers the agencies, the hospitals and the roads.</p>'
         + callout("<b>Frost first:</b> before you accept a policy-limits offer from the other driver's insurer, call. Accepting it the wrong way can cost you your own coverage.")
     ),
     sources=src("nextdoor_goose_creek", "scdoi") + [("S.C. Code §§ 38-77-140, 38-77-150 and 38-77-160 (minimum, UM and UIM coverage)", "https://www.scstatehouse.gov/code/t38c077.php", False)],
     related=[CAR + "/uninsured-motorist-accidents", CAR + "/hit-and-run-accidents", "areas/goose-creek"],
     faqs=[("Will using my uninsured motorist coverage raise my rates?", "No. South Carolina prohibits surcharging you for a claim arising from a crash you did not cause."),
           ("Do I have UIM coverage?", "Check the declarations page of your policy for underinsured motorist limits. If it is missing, ask us to review the offer form; improperly offered UIM coverage can be read into the policy.")])
