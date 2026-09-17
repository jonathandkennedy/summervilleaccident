"""Answer pages built from what people actually search and ask (Search Console, keyword research, and the community
threads on Reddit, Nextdoor, Justia and Avvo where Lowcountry drivers ask each other), plus the /questions/ hub that
collects every question answered on the site. Each answer page links out to where the question gets asked."""
from .base import page, A, ext, img, p, ul, checks, steps, callout, answer, band, esc, table
from . import firm
from .local import cite, link, LINKS

HUB = firm.CAR
TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'


def sp(slug, **kw):
    kw.setdefault("kind", "spoke")
    kw.setdefault("hub", HUB)
    kw.setdefault("eyebrow", "Car accidents · Summerville, SC")
    kw.setdefault("author", "tara")
    kw.setdefault("priority", 0.7)
    return page(slug, **kw)


def asked(*keys, intro="This question comes up constantly in the places Lowcountry drivers ask each other:"):
    """A short 'where people ask this' block linking (nofollow) to the community threads and Q&A boards."""
    lis = "".join(f"<li>{link(k)}</li>" for k in keys if k in LINKS)
    return (f'<h2>Where people ask this</h2><p>{intro}</p><ul>{lis}</ul>'
            '<p>Most of the answers in those threads are from other drivers, and some are wrong for South Carolina. The answer above is the law here, written by an attorney who handles these claims. If your situation is different, ask us; the call is free.</p>')


# ----------------------------------------------------------------------------- 1. Getting the report
sp(HUB + "/how-to-get-your-south-carolina-accident-report",
   title="How to Get Your South Carolina Accident Report | FR-10, TR-310 & SCDMV",
   description="How to get a copy of your car accident report in South Carolina: what the FR-10 you were handed is, how to request the full TR-310 collision report from the SCDMV or the agency, where the report number is, and what to do if the report is wrong.",
   h1="How to get your South Carolina accident report (and what to do if it is wrong)",
   summary="The FR-10 you were handed, the full TR-310 report, how to request it from the SCDMV or the police, and how to challenge a mistake.",
   lead="The report is the first thing every insurer reads. Here is how to get it, what each form is, and what the fault codes on it actually mean.",
   body=(
       answer(f"At the scene, the officer gives each driver a Form FR-10, which shows the report number, the investigating agency and the other driver's insurance. The full collision report (Form TR-310) is filed by the officer within days and is available a week or two later: for Highway Patrol crashes, request it from the {link('scdmv_collision_report', 'SCDMV')} using the report number; for a town or county crash, request it from that police department or sheriff's office. There is a small fee. If no officer came, you must file Form FR-309 with the SCDMV within 15 days ({cite('report_dmv')}). A wrong fault code on the report is an opinion, not a verdict, and can be overcome with evidence.")
       + '<h2>The three forms, and what each one is for</h2>'
       + table(["Form", "What it is", "Who gives it to you"], [
           ["FR-10 (Insurance Verification)", "The one-page form the officer hands each driver at the scene: report number, agency, officer, date, location, the other driver's name and insurer. It is proof of insurance verification and the key to opening a claim.", "The investigating officer, at the scene"],
           ["TR-310 (Traffic Collision Report)", "The full report: the officer's narrative and diagram, contributing factors and citations, road and weather conditions, vehicles, occupants, injuries, witnesses and the location by route and mile marker.", "The SCDMV (Highway Patrol crashes) or the local agency, on request, usually 7 to 14 days after the crash"],
           ["FR-309 (Driver's Report)", "The form a driver must file with the SCDMV within 15 days when no officer investigated and there was injury, death or property damage over $1,000.", "You file it yourself"],
       ])
       + '<h2>Who has your report</h2>'
       + checks([
           f"<b>I-26, I-526, I-95 and most state highways outside town limits:</b> the {link('schp', 'South Carolina Highway Patrol')}. Request the TR-310 through the {link('scdmv_collision_report', 'SCDMV collision report page')} with the report number from your FR-10.",
           f"<b>Inside Summerville:</b> the {link('summerville_pd', 'Summerville Police Department')} records division.",
           "<b>Goose Creek, North Charleston, Charleston, Mount Pleasant, Moncks Corner and Walterboro:</b> that city's police department.",
           f"<b>Unincorporated Dorchester County:</b> the {link('dorchester_sheriff', 'Dorchester County Sheriff’s Office')}; Berkeley and Charleston County crashes, those sheriffs' offices.",
           "<b>Not sure?</b> The agency name is printed on your FR-10. If you lost the FR-10, tell us the date and location and we will find it.",
       ])
       + '<h2>Where the report number is</h2>'
       + '<p>The collision report number is printed on the FR-10 near the top, alongside the agency and officer. Insurers ask for it on the first call, and the SCDMV request form requires it. If you were taken from the scene by ambulance and never received an FR-10, the officer can provide one afterward, or the number can be found by date, location and your name.</p>'
       + '<h2>What the report does, and does not, decide</h2>'
       + f'<p>The TR-310 records the officer\'s opinion of the contributing factors (following too closely, failure to yield, distraction) and any citation issued. Insurers treat it as strong evidence, and it usually is. It is not a legal finding of fault. Officers arrive after the crash, spend a limited time at the scene, and rarely see the video or the vehicle data. We have had reports corrected with surveillance footage, event-data-recorder downloads and witness statements the officer never took. If the report blames you and you know it is wrong, do not accept it; {A(HUB + "/south-carolina-comparative-negligence", "fault is a percentage")}, and it is decided on all the evidence.</p>'
       + '<h2>Correcting a mistake</h2>'
       + steps([
           ("Factual errors", " (wrong plate, wrong insurer, wrong direction of travel) can be corrected by the investigating agency through a supplemental report. Contact the officer or the records division with the report number."),
           ("Opinion errors", " (the contributing-factor codes, the diagram) are rarely amended. They are answered with evidence in the claim and, if necessary, in court."),
           ("Missing witnesses", " can give statements later. Get them to us early, while memories are fresh."),
       ])
       + '<h2>What we do with it</h2>'
       + '<p>We obtain the TR-310, the 911 audio, the officer\'s body-camera and dash-camera video and any supplemental reports for every client at no cost, read them against the physical evidence, and send preservation demands for anything the report shows exists (a named witness, a business camera, the other vehicle). The report is the start of the investigation, not the end.</p>'
       + asked("reddit_charleston_accidents", "reddit_southcarolina_accidents", "justia_sc_car", "scdoi_faq")
       + callout("<b>Frost first:</b> if you are calling the other driver's insurer to “give them the report number,” stop there. The number is all they need from you. The rest of that conversation is for their benefit.")
   ),
   faqs=[
       ("How long does it take to get an accident report in South Carolina?", "Usually one to two weeks after the crash for the full TR-310. The FR-10 is given to you at the scene."),
       ("How much does a South Carolina accident report cost?", "The SCDMV and most agencies charge a small fee for a copy. We obtain it for clients at no cost."),
       ("What if the police report says I was at fault?", "The report records the officer's opinion, not a legal finding. Fault is decided on all the evidence, and reports are regularly overcome with video, vehicle data and witness statements."),
       ("Can I get the other driver's insurance information from the report?", "Yes. The FR-10 lists the other driver's insurer at the scene, and the TR-310 repeats it. We verify the policy was actually in force; many are not."),
   ],
   sources=[("S.C. Code § 56-5-1270 (accident reports to the DMV)", "https://www.scstatehouse.gov/code/t56c005.php", False), ("SCDMV – collision reports", "https://www.scdmvonline.com/Driver-Services/Reports/Collision-Reports", False)],
   related=[HUB + "/what-to-do-after-a-car-accident-in-south-carolina", HUB + "/car-accident-without-a-police-report", "blog/i-26-crash-summerville-who-writes-the-report"])

# ----------------------------------------------------------------------------- 2. No police report
sp(HUB + "/car-accident-without-a-police-report",
   title="Can You Claim a Car Accident Without a Police Report in South Carolina?",
   description="Yes, but it is harder. How an injury or property-damage claim works in South Carolina when no officer came to the scene, the FR-309 you must file within 15 days, the hit-and-run exception, and how to prove what happened without a report.",
   h1="Can you make a car accident claim without a police report in South Carolina?",
   summary="Yes, but it is harder. The FR-309 you must file, the hit-and-run exception, and how to prove the crash without an officer's report.",
   lead="No officer came, or you agreed to “handle it between yourselves,” and now you are hurt. Here is where you stand.",
   body=(
       answer(f"Yes. A police report is not legally required to make an insurance claim or file a lawsuit in South Carolina. But without one, the other driver's insurer will question whether the crash happened as you describe, and you will need other evidence: photos, the other driver's information, witnesses, your own prompt written account, and same-day medical records. If no officer investigated and there was injury or property damage over $1,000, you must file Form FR-309 with the SCDMV within 15 days ({cite('report_dmv')}). The exception is a hit-and-run by an unidentified driver: an uninsured motorist claim for that requires a prompt police report.")
       + '<h2>Why there is no report</h2>'
       + checks([
           "The crash seemed minor and both drivers agreed to exchange information and leave.",
           "Police were called but did not respond to a no-injury crash on private property (a parking lot), which some agencies do not investigate.",
           "The other driver talked you out of calling (“let's not involve insurance”), which is often the first sign they had none.",
           "You were hurt, went to the hospital, and nobody called it in.",
       ])
       + '<h2>What to do now, in order</h2>'
       + steps([
           ("File the FR-309 with the SCDMV within 15 days.", " It is the driver's own report and it satisfies the reporting statute. Do it even if the deadline has passed; late is better than never."),
           ("Write down everything today.", " Date, time, exact location, weather, what each vehicle did, what the other driver said, and every name and phone number you collected. Sign and date it."),
           ("Report the crash to your own insurer.", " Your policy requires prompt notice regardless of a police report, and your own coverage may be what pays."),
           ("Get medical care and say it was a car crash.", " The medical record dated the day of the crash becomes the document that proves when and how you were hurt."),
           ("Go back to the scene.", " Photograph it, note the businesses and homes with cameras, and ask them to preserve footage. Most systems overwrite within days."),
           ("Do not accept the other driver's version by silence.", " If they tell their insurer a different story, the first written account wins credibility. Make yours first."),
       ])
       + '<h2>The hit-and-run exception</h2>'
       + f'<p>If the driver left and cannot be identified, your claim is against your own uninsured motorist coverage, and South Carolina requires that a hit-and-run be reported to law enforcement promptly for that claim to be paid. Report it now, even days later; a late report is better than none. {A(HUB + "/hit-and-run-accidents", "Hit-and-run claims")}.</p>'
       + '<h2>Parking-lot crashes</h2>'
       + '<p>Many crashes without a report happen in the parking lots along Dorchester Road, North Main Street and Highway 17-A. Some agencies do not investigate private-property collisions without injury. The rules of the road still apply by analogy, and the store\'s cameras usually recorded it. Ask the manager the same day.</p>'
       + '<h2>How the claim goes</h2>'
       + '<p>Expect the other driver\'s insurer to say it cannot confirm the crash occurred, or that its driver reports a different story. That is answered with the evidence above, with the property-damage estimates that show how the vehicles hit, and with the medical records. It takes more work than a claim with a report, and it is done regularly.</p>'
       + asked("reddit_legaladvice_sc", "reddit_insurance_sc", "justia_sc_car", "scdoi_faq")
       + callout("<b>Frost first:</b> the next time you are in a crash, however minor it looks, call 911 and wait. The ten minutes it costs is the cheapest evidence you will ever get.")
   ),
   faqs=[
       ("Is it illegal not to report a car accident in South Carolina?", "A crash with injury, death or property damage of $1,000 or more must be reported to law enforcement immediately, and to the SCDMV within 15 days if no officer investigated. Failing to report can affect your license and your claim."),
       ("Can I file a police report days after the accident?", "You can make a report to the agency after the fact, and you should. It will be a delayed report rather than an investigation, but it documents the crash, and for a hit-and-run it is required."),
       ("Will the insurance company deny my claim without a police report?", "It may try. A report is not required by law; the claim is proved with other evidence. We build that evidence for clients whose crashes were never investigated."),
   ],
   sources=[("S.C. Code §§ 56-5-1260 and 56-5-1270 (accident reports)", "https://www.scstatehouse.gov/code/t56c005.php", False), ("S.C. Code § 38-77-150 (uninsured motorist coverage)", "https://www.scstatehouse.gov/code/t38c077.php", False)],
   related=[HUB + "/how-to-get-your-south-carolina-accident-report", HUB + "/hit-and-run-accidents", HUB + "/minor-car-accident-what-to-do"])

# ----------------------------------------------------------------------------- 3. Claiming injury later
sp(HUB + "/how-long-after-a-car-accident-can-you-claim-injury",
   title="How Long After a Car Accident Can You Claim an Injury in South Carolina?",
   description="You felt fine at the scene and hurt three days later. How long you have to see a doctor and claim an injury after a South Carolina crash, why delayed symptoms are normal, what insurers do with a treatment gap, and the three-year legal deadline.",
   h1="How long after a car accident can you claim an injury?",
   summary="Delayed pain is normal. What the law allows, what insurers argue about a gap, and why the practical answer is 'this week.'",
   lead="You said “I'm fine” at the scene. Three days later you cannot turn your head. Here is what that does to your claim, and what to do now.",
   body=(
       answer(f"Legally, you have three years from the crash to file an injury lawsuit in South Carolina ({cite('sol_injury')}), and there is no statute that says an injury reported after a certain number of days does not count. Practically, the longer the gap between the crash and your first medical visit, the harder the insurer will argue the injury came from something else. Delayed symptoms from whiplash, concussion and disc injuries are medically normal; see a doctor as soon as symptoms appear, tell the provider it was a car crash, and notify the insurer that you are injured. A claim opened for property damage only can be expanded to injury.")
       + '<h2>Why you felt fine and now you don\'t</h2>'
       + '<p>Adrenaline suppresses pain for hours. Soft-tissue injuries to the neck and back stiffen and inflame over one to three days. Concussion symptoms (headache, fog, sleep problems, irritability) often appear after the first night. Disc injuries can take a week or more to produce the radiating pain or numbness that finally sends someone to a doctor. Emergency physicians expect this; insurance adjusters pretend not to.</p>'
       + '<h2>The legal answer</h2>'
       + checks([
           f"<b>Three years</b> from the date of the crash to file suit for injury ({cite('sol_injury')}); two years if a government vehicle or agency is involved.",
           "<b>No cutoff for reporting an injury.</b> There is no 72-hour rule, 14-day rule or 30-day rule in South Carolina law. Those numbers come from other states' no-fault systems or from insurers' internal guidelines.",
           "<b>Your own policy</b> requires prompt notice of the crash, not a diagnosis. Reporting the crash on day one preserves your coverage; the injury can be added when it appears.",
       ])
       + '<h2>The practical answer</h2>'
       + steps([
           ("Same day or next day is ideal.", " It protects your health and creates the record that ties the injury to the crash."),
           ("Within a week is fine and common.", " Tell the provider when the crash happened and when symptoms began. That sequence is the medically expected one, and the chart says so."),
           ("Weeks later is explainable, but you need to explain it.", " Why you waited (you hoped it would resolve, you could not get an appointment, you had no insurance), and what changed. Then stay in treatment without gaps."),
           ("Months later is a hard case.", " Not impossible, especially with a documented mechanism and an injury that fits it, but expect the insurer to fight, and call us before you contact them."),
       ])
       + '<h2>What insurers do with a gap</h2>'
       + '<p>Every day between the crash and the first visit is a day the adjuster will suggest you were hurt somewhere else: at work, at the gym, in an earlier accident, or not at all. The first medical record after the crash is therefore the most important document in the claim. Get it soon, make it accurate, and then follow the treatment plan, because a second gap (between visits) is the next argument.</p>'
       + '<h2>I already told the adjuster I was not hurt</h2>'
       + f'<p>That is the most common regret we hear, and it is survivable. What you said at the scene or on day two was true when you said it. What matters now is the medical record showing when symptoms appeared and what they are. Do not give another recorded statement to explain; let us handle the correction in writing. {A(HUB + "/should-i-talk-to-the-other-drivers-insurance-company", "Why the recorded statement matters")}.</p>'
       + asked("reddit_legaladvice_sc", "reddit_charleston_accidents", "justia_sc_injury", "avvo_sc_car")
       + callout("<b>Frost first:</b> if you are reading this because you hurt today and the crash was last week, make the doctor's appointment before you finish the page. Then call us.")
   ),
   faqs=[
       ("How long after a car accident can you go to the hospital?", "Any time, and you should go as soon as symptoms appear. There is no legal cutoff. The sooner the visit, the clearer the link between the crash and the injury."),
       ("Can I reopen a claim I already settled if I get worse?", "Generally no. A signed release ends the claim even if you later need surgery. That is why we tell clients never to sign before treatment is finished."),
       ("Does whiplash show up right away?", "Often not. Neck stiffness and pain commonly peak one to three days after a crash. See a doctor when it appears and describe the crash."),
       ("Is there a 14-day rule in South Carolina?", "No. That rule is from Florida's no-fault system. South Carolina has no deadline for seeking treatment, only the three-year deadline to file suit."),
   ],
   sources=[("S.C. Code § 15-3-530 (three-year limitations period)", "https://www.scstatehouse.gov/code/t15c003.php", False)],
   related=[HUB + "/auto-injury-assessment-after-a-crash", HUB + "/south-carolina-car-accident-statute-of-limitations", HUB + "/rear-end-collisions"])

# ----------------------------------------------------------------------------- 4. Not your fault
sp(HUB + "/car-accident-that-was-not-your-fault",
   title="Car Accident That Was Not Your Fault in South Carolina | What Happens Next",
   description="What to do after a car accident that was not your fault in South Carolina: how the other driver's insurer handles your car, the rental, the total-loss value and diminished value, why your own policy may still be the faster route, and what never to sign.",
   h1="What to do after a car accident that was not your fault",
   summary="The other driver's insurer owes you. How the car, the rental, the total-loss value, diminished value and the injury claim actually get paid.",
   lead="The other driver ran the light and admitted it. You would think the rest is simple. Here is how it actually goes, and how to keep it simple.",
   body=(
       answer(f"When another driver caused the crash in South Carolina, that driver's liability insurer owes you for your vehicle (repair or actual cash value if totaled), a rental or loss-of-use while it is being fixed, the diminished value of a repaired car, your medical expenses, lost income, and pain and suffering. You are not required to give that insurer a recorded statement or sign a medical authorization. You may use your own collision coverage to fix the car faster and let your insurer recover from the at-fault carrier, including your deductible. The property-damage claim and the injury claim are separate; settle the car, never the injury, early.")
       + '<h2>Two claims, two speeds</h2>'
       + table(["", "Property damage (the car)", "Bodily injury (you)"], [
           ["Who pays", "The at-fault driver's insurer, or your own collision coverage (which then recovers from them)", "The at-fault driver's insurer, plus your UM/UIM coverage if their limits are too low"],
           ["Timing", "Days to a few weeks", "Months; it should not settle until treatment is finished"],
           ["Statement needed?", "Basic facts only. No recorded statement about injuries.", "None. Your lawyer provides what is needed in writing."],
           ["Release", "Read it. Some property-damage releases quietly include injury.", "Never sign early. It ends the claim permanently."],
       ])
       + '<h2>The car</h2>'
       + steps([
           ("Repair or total loss.", " The insurer chooses the cheaper of repairing the car or paying its actual cash value (what a comparable car sells for locally, not what you owe on it). Get your own comparable listings if the offer is low; the valuation reports insurers use are negotiable."),
           ("Rental or loss of use.", " The at-fault insurer owes a rental for a reasonable repair period, or a daily loss-of-use amount if you do not rent. Ask for it; it is not offered automatically."),
           ("Diminished value.", " A repaired car is worth less than one never wrecked. South Carolina lets you claim that difference from the at-fault insurer. It is real money on a newer car, and most people never ask."),
           ("Your own collision coverage.", " Often faster: your insurer pays, then recovers from the at-fault carrier and refunds your deductible. Using it does not raise your rates for a crash you did not cause."),
           ("Gap insurance and loans.", " If you owe more than the car is worth, the insurer pays the value, not the loan. Gap coverage, if you bought it, covers the difference."),
       ])
       + '<h2>The injury claim</h2>'
       + f'<p>The at-fault insurer will open a bodily-injury claim, assign an adjuster, and call. Everything on {A(HUB + "/should-i-talk-to-the-other-drivers-insurance-company", "what to say to the other driver’s insurer")} applies: give the claim number and your lawyer\'s name, and nothing else. Your medical bills are paid now by your health insurance or MedPay, and reimbursed at settlement. The claim is valued once your treatment is complete, on the full record. {A(HUB + "/how-much-is-my-car-accident-case-worth", "How a case is valued")}.</p>'
       + '<h2>“They admitted it was their fault”</h2>'
       + f'<p>Helpful, and not the end of it. The insurer is not bound by what its driver said at the scene, and a driver who apologized on Tuesday often remembers it differently by Friday. Get the admission into the police report and, if you can, a text or voicemail. Then expect the adjuster to look for some fault in you anyway; that is the {A(HUB + "/south-carolina-comparative-negligence", "comparative negligence")} game, and it is played in every claim.</p>'
       + '<h2>If their limits are too low, or they have none</h2>'
       + f'<p>The state minimum is $25,000 per person. If your injury is worth more, or the driver was uninsured, your own uninsured and underinsured motorist coverage pays the rest. Do not accept a policy-limits offer without your own insurer\'s written consent, or you can forfeit that coverage. {A(HUB + "/uninsured-motorist-accidents", "UM and UIM claims")}.</p>'
       + asked("reddit_charleston_accidents", "reddit_insurance_sc", "reddit_southcarolina_accidents", "scdoi_faq")
       + callout("<b>Frost first:</b> the property-damage adjuster is often friendly and fast, and the bodily-injury adjuster arrives right behind them with a small check and a release. Handle the car yourself if you like. Do not handle the injury.")
   ),
   faqs=[
       ("Do I have to use my own insurance if the accident was not my fault?", "No, but you may want to for the car: your collision coverage is usually faster, your insurer recovers from the at-fault carrier, and your deductible comes back. Your rates cannot be raised for a crash you did not cause."),
       ("Who pays for my rental car after an accident that was not my fault?", "The at-fault driver's insurer, for a reasonable repair period, or a daily loss-of-use payment if you do not rent. Ask; it is not offered unprompted."),
       ("Can I get diminished value in South Carolina?", "Yes. South Carolina allows a claim against the at-fault driver's insurer for the loss in a repaired vehicle's market value."),
       ("The other driver's insurer wants a recorded statement before paying for my car. Do I have to?", "No. Give the basic facts of the collision in writing if needed for the property claim, and nothing about your injuries. We handle it for clients."),
   ],
   sources=[("SC Department of Insurance – auto insurance FAQs", "https://www.doi.sc.gov/983/FAQs-Auto-Insurance", False), ("S.C. Code § 38-77-140 (minimum liability coverage)", "https://www.scstatehouse.gov/code/t38c077.php", False)],
   related=[HUB + "/should-i-talk-to-the-other-drivers-insurance-company", HUB + "/how-much-is-my-car-accident-case-worth", HUB + "/uninsured-motorist-accidents"])

# ----------------------------------------------------------------------------- 5. Minor accident
sp(HUB + "/minor-car-accident-what-to-do",
   title="What to Do After a Minor Car Accident in South Carolina | Do You Need a Lawyer?",
   description="A fender-bender in a Summerville parking lot or on Main Street: what South Carolina requires you to do, when you can handle it yourself, when a 'minor' crash is not, and an honest answer to whether you need a lawyer.",
   h1="What to do after a minor car accident, and whether you need a lawyer",
   summary="An honest answer: most fender-benders do not need a lawyer. Here is how to handle one, and the signs that yours is not minor.",
   lead="Most crashes are small. Most do not need us. Here is how to handle one yourself, and the four signs that you should call anyway.",
   body=(
       answer(f"After a minor crash in South Carolina, stop, exchange names, addresses, license and insurance information, photograph the damage, and call the police if there is any injury or the damage looks like it could exceed $1,000, which today means almost any crash with body damage ({cite('report_duty')}). Report it to your insurer. If nobody is hurt and the damage is small, you can usually handle the property claim yourself and do not need a lawyer. Call one if anyone has any symptoms, if fault is disputed, if the other driver has no insurance, or if the adjuster asks you to sign anything.")
       + '<h2>Handling it yourself</h2>'
       + steps([
           ("Exchange information and photograph everything.", " Both licenses, both insurance cards, both plates, all four corners of both cars, the scene. Thirty seconds of photos ends most later disputes."),
           ("Call the police if in doubt.", " Any injury, or damage that might exceed $1,000, must be reported immediately. Many agencies will take a report for a minor crash if you ask; some will not for private-property crashes with no injury. If no officer comes, file the FR-309 with the SCDMV within 15 days."),
           ("Report it to your insurer.", " Your policy requires it, and it protects you if the other driver later claims an injury. Reporting does not itself raise your rates for a crash you did not cause."),
           ("Decide who fixes the car.", " The at-fault driver's insurer, or your own collision coverage (faster, deductible refunded when they recover). Get two estimates if the first seems low."),
           ("Watch yourself for a week.", " Soft-tissue injuries appear over days. If anything hurts, see a doctor and tell them about the crash."),
       ])
       + '<h2>When a “minor” crash is not</h2>'
       + checks([
           "<b>Anyone has any symptoms</b>, including a child in the back seat. Neck pain, headache, dizziness, numbness. Low-speed rear-end crashes cause real injuries.",
           "<b>Fault is disputed.</b> If the other driver's story differs from yours, the crash is no longer minor; it is a credibility contest, and the recorded statement they want from you is the weapon.",
           "<b>The other driver is uninsured, or their insurer is not responding.</b> Your UM coverage and the rules around it get complicated fast.",
           "<b>An adjuster sends a release or a check.</b> A release for property damage that quietly includes bodily injury is common. Read it, or send it to us.",
           "<b>The other vehicle was commercial</b> (a delivery van, a work truck, a rideshare). Different insurers, different rules.",
       ])
       + '<h2>The honest answer about lawyers</h2>'
       + '<p>A lawyer on a contingency fee makes sense when there is an injury claim to value and an insurer to negotiate with. On a property-damage-only claim, a lawyer\'s percentage would come out of money you could collect yourself. We tell people that on the phone every week, and we walk them through the property claim for free. If an injury appears later, the conversation changes, and the call is still free.</p>'
       + '<h2>Small claims</h2>'
       + '<p>If the at-fault insurer will not pay a small property claim fairly, South Carolina magistrate court hears civil claims up to $7,500 without a lawyer, in the county where the crash happened. Bring your photos, estimates and the report.</p>'
       + asked("reddit_charleston_accidents", "reddit_summerville_accidents", "reddit_insurance_sc", "scdoi_faq")
       + callout("<b>Frost first:</b> “minor” is a judgment made at the scene, with adrenaline, before anyone has seen a doctor. Take the photos and the report as if it were not, and you lose nothing if it was.")
   ),
   faqs=[
       ("Do I have to report a minor accident in South Carolina?", "If anyone is hurt or property damage is $1,000 or more, yes, immediately to law enforcement, and to the SCDMV within 15 days if no officer investigated. Modern body damage exceeds $1,000 quickly."),
       ("Should I get a lawyer for a fender bender?", "Usually not, if nobody is hurt and fault is clear. Call one if anyone has symptoms, fault is disputed, the other driver is uninsured, or you are asked to sign anything."),
       ("Will a minor accident raise my insurance rates?", "South Carolina prohibits insurers from surcharging you for a crash you did not cause. An at-fault crash can affect rates depending on your policy."),
       ("Can I sue for a minor car accident?", "Yes, in magistrate court for claims up to $7,500 without a lawyer, or in the Court of Common Pleas for larger claims. Most small claims settle with the insurer."),
   ],
   sources=[("S.C. Code § 56-5-1260 (duty to report)", "https://www.scstatehouse.gov/code/t56c005.php", False), ("SC Department of Insurance – auto insurance FAQs", "https://www.doi.sc.gov/983/FAQs-Auto-Insurance", False)],
   related=[HUB + "/car-accident-that-was-not-your-fault", HUB + "/car-accident-without-a-police-report", HUB + "/rear-end-collisions"])

# ----------------------------------------------------------------------------- 6. Your fault
sp(HUB + "/what-happens-if-the-accident-was-my-fault",
   title="What Happens After a Car Accident That Was Your Fault in South Carolina?",
   description="If you caused a crash in South Carolina: what your liability insurance does, what happens if the other driver sues, why you may still recover for your own injuries under the 50 percent rule, and why the citation is not the last word on fault.",
   h1="What happens if the car accident was my fault?",
   summary="Your liability coverage, the possibility of being sued, and why you can still recover for your own injuries if you were 50 percent or less at fault.",
   lead="The officer wrote you up. You are worried about the other driver, your rates, and your own injuries. Here is what actually happens.",
   body=(
       answer(f"If you caused a crash in South Carolina, your liability insurance pays the other driver's damages up to your policy limits and provides a lawyer to defend you if you are sued. Your own injuries and vehicle are covered by your collision, medical-payments and health coverage, not by the other driver. Fault is rarely all-or-nothing: under South Carolina's comparative negligence rule you can still recover from the other driver for your own injuries if your share of fault was 50 percent or less, reduced by that share. A citation is evidence, not a verdict, and paying it is treated as a guilty plea.")
       + '<h2>What your insurance does</h2>'
       + checks([
           "<b>Liability coverage</b> pays the other people's injuries and property damage up to your limits (at least 25/50/25 in South Carolina). If their damages exceed your limits, you can be personally exposed for the rest, which is why higher limits and umbrella policies matter.",
           "<b>Defense.</b> If the other driver sues you, your insurer must provide and pay for a lawyer. Notify your insurer immediately if you receive a summons; you generally have 30 days to respond.",
           "<b>Collision coverage</b> fixes your own car, less your deductible. Without it, your car is your cost.",
           "<b>MedPay and health insurance</b> pay your own medical bills.",
       ])
       + '<h2>Fault is a percentage</h2>'
       + f'<p>Officers assign contributing factors at the scene; insurers and juries assign percentages on all the evidence. A driver who was cited for failure to yield while the other driver was speeding and texting may be found 40 percent at fault, which means recovering 60 percent of their own damages from the other driver. If you were partly at fault and hurt, do not assume you have no claim. {A(HUB + "/south-carolina-comparative-negligence", "How the 51 percent rule works")}.</p>'
       + '<h2>The citation</h2>'
       + '<p>Paying the citation is a guilty plea, and a guilty plea can be used in the civil case as an admission. Many people pay it to make it go away and only later learn it decided their injury claim. Before you pay, at least ask. The citation itself is handled in the criminal or magistrate court; this site does not handle that, and the firm\'s main site explains who does. What we handle is your injury claim, and the citation matters to it.</p>'
       + '<h2>If the other driver sues you</h2>'
       + steps([
           ("Send the papers to your insurer the day you receive them.", " Late notice can cost you the defense."),
           ("Do not contact the other driver or their lawyer.", " Your insurer's lawyer does that."),
           ("Understand the limits question.", " If the claim may exceed your policy limits, ask your insurer's lawyer in writing whether the insurer is settling within limits. Insurers that refuse a reasonable within-limits settlement can be responsible for an excess verdict."),
       ])
       + '<h2>If you were hurt too</h2>'
       + '<p>Your own injury claim against the other driver depends on their share of fault. The evidence that reduces your percentage (their speed, their phone, the signal timing, the video) is the same evidence a defense lawyer would want, and it disappears on the same schedule. If you were hurt and the fault is not clear-cut, call us before you talk to either insurer.</p>'
       + asked("reddit_legaladvice_sc", "reddit_insurance_sc", "justia_sc_car", "scdoi_faq")
       + callout("<b>Frost first:</b> “it was my fault” is a conclusion, and you are not qualified to reach it at the scene any more than the other driver is. Describe what happened. Let the evidence assign the percentages.")
   ),
   faqs=[
       ("Can I still get compensation if the accident was partly my fault in South Carolina?", "Yes, if your share of fault was 50 percent or less. Your recovery is reduced by your percentage."),
       ("Will I be sued if I caused a car accident?", "Usually the other driver's claim is settled by your insurer without a lawsuit. If you are sued, your insurer provides a lawyer. Notify them immediately."),
       ("Does paying a citation admit fault in a civil case?", "Paying it is a guilty plea, which can be used as an admission in the injury claim. Ask before you pay."),
       ("What if the other driver's damages exceed my insurance limits?", "You can be personally responsible for the excess. Tell your insurer's lawyer in writing that you want the claim settled within your limits if a reasonable opportunity exists."),
   ],
   sources=[("S.C. Code § 15-38-15 (apportionment of fault)", "https://www.scstatehouse.gov/code/t15c038.php", False), ("S.C. Code § 38-77-140 (minimum liability coverage)", "https://www.scstatehouse.gov/code/t38c077.php", False)],
   related=[HUB + "/south-carolina-comparative-negligence", HUB + "/is-south-carolina-an-at-fault-state", HUB + "/car-accident-that-was-not-your-fault"])

# ----------------------------------------------------------------------------- 7. Rear-end
sp(HUB + "/rear-end-collisions",
   title="Rear-End Collision Lawyer | Summerville, SC | Whiplash & Fault Rules",
   description="Rear-ended on Main Street, Dorchester Road or I-26? Who is at fault in a South Carolina rear-end collision, the 'sudden stop' defense, chain-reaction crashes, whiplash and concussion claims, and why low-speed does not mean low-injury.",
   h1="Rear-end collisions in Summerville: fault, whiplash and the low-speed myth",
   summary="The most common crash in Summerville. Who is at fault, the sudden-stop and chain-reaction defenses, and why low speed does not mean low injury.",
   lead="Stop-and-go traffic on North Main Street, Dorchester Road and the 17-A exits produces more rear-end collisions than any other kind of crash here. They are also the ones insurers fight hardest on injury.",
   body=(
       answer(f"In South Carolina the driver who hits a vehicle from behind is almost always at fault, because every driver must keep a safe following distance and be able to stop ({cite('report_duty', 'S.C. Code § 56-5-1930')}). The exceptions are narrow: the front driver reversed, stopped suddenly without reason where a stop was not expected, or had no working brake lights. Rear-end crashes cause whiplash, concussion and disc injuries even at low speeds, and the insurer's main defense is not fault but injury: that a crash with little visible damage could not have hurt you. Medical records and the vehicle's crush data answer that.")
       + '<h2>Fault, and the exceptions</h2>'
       + checks([
           "<b>The presumption.</b> Following too closely is a violation, and the rear driver is presumed negligent. In most rear-end claims fault is not seriously disputed.",
           "<b>Sudden stop.</b> The rear driver's usual argument. It fails when the stop was for traffic, a signal, a pedestrian or a turning vehicle, because those are the stops a following driver must anticipate. It has some force when the front driver stopped in a travel lane for no reason.",
           "<b>Brake lights.</b> If yours were out, expect a comparative-fault argument. Photograph them working after the crash.",
           "<b>Reversing.</b> A car backing into another at a light or in a parking lot is a different crash; the reversing driver is at fault.",
           "<b>Chain reactions.</b> When car C hits car B into car A, C is usually at fault for both, unless B had already hit A. The order of impacts is proved with damage patterns and witness accounts, and it decides which insurer pays whom.",
       ])
       + '<h2>The injuries</h2>'
       + '<p>Whiplash (cervical strain), concussion from the head snapping forward and back, thoracic and lumbar strains, and disc herniations in the neck and low back. Symptoms typically peak one to three days after the crash. Most resolve with weeks of treatment; a meaningful share do not, and become chronic pain, headaches or radiating nerve symptoms that require injections or surgery. Older drivers and people with prior neck or back problems are hurt more by the same impact, and South Carolina law lets you recover for the aggravation of a pre-existing condition.</p>'
       + '<h2>The low-speed defense</h2>'
       + '<p>Because a rear-end crash at 10 miles per hour may leave little visible damage, insurers argue “minor impact, soft tissue” and offer little. The argument is not medicine. Bumpers are designed to absorb low-speed impacts without visible damage while the occupants absorb the acceleration; the injury depends on the change in velocity, head position, headrest height and the occupant, not the repair bill. We answer it with the medical records, the treating doctor\'s opinion, the repair estimate\'s hidden-damage findings, and, in a serious case, the vehicle\'s event data.</p>'
       + '<h2>Where they happen</h2>'
       + f'<p>North Main Street from downtown to the interstate, Dorchester Road through Oakbrook, the Bacons Bridge Road and Berlin G. Myers Parkway signals, the I-26 exit 199 and 203 ramps, and Highway 17-A through Nexton. Most involve a distracted following driver in stop-and-go traffic. {A(HUB + "/distracted-driving-accidents", "Proving the driver was on the phone")} and {A(HUB + "/where-crashes-happen-in-summerville", "where crashes cluster")}.</p>'
       + '<h2>What to do</h2>'
       + f'<p>Everything on the {A(HUB + "/what-to-do-after-a-car-accident-in-south-carolina", "first-48-hours checklist")}, plus: photograph your brake lights working and your headrest position, note whether you saw the other driver looking down, and see a doctor within a day or two even if you only feel stiff. Do not tell the adjuster you were “just sore.”</p>'
       + asked("reddit_charleston_accidents", "reddit_legaladvice_sc", "reddit_insurance_sc", "justia_sc_car")
       + callout("<b>Frost first:</b> the two sentences that cost rear-end victims the most are “I'm just a little sore” to the adjuster and “I don't need to go to the doctor” to themselves. Both are usually said in the first 48 hours.")
   ),
   faqs=[
       ("Is the rear driver always at fault in South Carolina?", "Almost always. Drivers must keep a safe following distance. The exceptions are a sudden unexplained stop, no brake lights, or the front car reversing."),
       ("How much is a rear-end whiplash claim worth?", "It depends on the treatment needed, how long symptoms last, lost work and the effect on daily life. Claims range from modest to substantial when injections or surgery are required. We give an honest range once the records are in."),
       ("What if I was hit from behind and pushed into the car in front of me?", "The driver who started the chain is usually responsible for both impacts. The order of impacts is proved with damage patterns and witness statements."),
       ("Can I claim if there was hardly any damage to my car?", "Yes. Injury depends on the forces on your body, not the repair estimate. Bumpers hide low-speed damage by design."),
   ],
   sources=[("S.C. Code § 56-5-1930 (following too closely)", "https://www.scstatehouse.gov/code/t56c005.php", False)],
   related=[HUB + "/how-long-after-a-car-accident-can-you-claim-injury", HUB + "/distracted-driving-accidents", HUB + "/auto-injury-assessment-after-a-crash"])

# ----------------------------------------------------------------------------- 8. Case worth
sp(HUB + "/how-much-is-my-car-accident-case-worth",
   title="How Much Is My Car Accident Case Worth in South Carolina? | Honest Answer",
   description="How a South Carolina car accident claim is actually valued: medical expenses, future care, lost income, pain and suffering, comparative fault, policy limits and liens. Why 'average settlement' numbers are meaningless, and what moves the value up or down.",
   h1="How much is my car accident case worth in South Carolina?",
   summary="How claims are actually valued, why 'average settlement' figures mislead, and what moves the number up or down.",
   lead="Every search for “average car accident settlement in South Carolina” returns a number somebody made up. Here is how the value is actually determined.",
   body=(
       answer("A South Carolina car accident claim is worth the sum of your economic damages (medical bills to date, future medical care, lost wages and lost earning capacity, property damage) plus non-economic damages (pain, suffering, disfigurement and loss of enjoyment of life), reduced by your percentage of fault if any, and limited in practice by the insurance available, including your own UM/UIM coverage. Punitive damages are added when the other driver was reckless or impaired. There is no reliable average: a claim with two chiropractic visits and a claim with a spinal fusion are both “car accident cases.”")
       + '<h2>The components</h2>'
       + table(["Damages", "What counts", "How it is proved"], [
           ["Medical expenses", "Ambulance, ER, imaging, specialists, therapy, injections, surgery, medication, equipment. South Carolina generally lets you claim the amount billed, not the discounted amount paid.", "Bills and records"],
           ["Future medical care", "Care your doctors expect you will need after settlement", "Treating physician opinions; a life-care plan in serious cases"],
           ["Lost wages", "Pay you missed, including sick and vacation time you used", "Pay stubs, employer letter, tax returns"],
           ["Lost earning capacity", "Work you can no longer do, or advancement you will not have", "Vocational and economic experts in serious cases"],
           ["Pain and suffering", "Physical pain, emotional distress, loss of enjoyment of life, disfigurement", "Your records, your testimony, family and coworkers, photographs, a daily journal"],
           ["Property damage", "Repair or value, rental, diminished value, personal items", "Estimates, valuations, receipts"],
           ["Punitive damages", "Punishment for reckless or impaired driving", "The other driver's conduct; uncapped when impaired"],
       ])
       + '<h2>What moves the value up or down</h2>'
       + checks([
           "<b>The medical record.</b> Prompt treatment, consistent follow-up, specialist referrals and objective findings (imaging, positive tests) raise value. Gaps, missed appointments and vague complaints lower it.",
           f"<b>Fault.</b> Every percentage point assigned to you is a discount. {A(HUB + '/south-carolina-comparative-negligence', 'The 51 percent rule')}.",
           "<b>Permanence.</b> An injury that resolves in eight weeks and one that leaves a permanent restriction are valued very differently. Do not settle before your doctor can say which yours is.",
           "<b>Credibility.</b> Inconsistent statements, social media and exaggeration lower value more than anything else. Honesty about prior injuries raises it.",
           "<b>The insurance available.</b> A $500,000 injury against a $25,000 policy is a $25,000 recovery unless there is UM/UIM coverage, an employer, a bar or another defendant. Finding every policy is often the largest single factor.",
           "<b>Venue.</b> Insurers value the same claim differently depending on whether a Dorchester, Berkeley or Charleston County jury would decide it.",
           "<b>Liens.</b> Health insurers, Medicare, Medicaid and medical providers may have to be reimbursed from the settlement. Negotiating those down changes what you actually keep.",
           "<b>Trial readiness.</b> Claims handled by a firm that tries cases settle for more, because the insurer prices the risk of a verdict.",
       ])
       + '<h2>Why “average settlement” numbers are meaningless</h2>'
       + '<p>Websites publish figures like “$20,000 to $30,000” because the search is popular. No such statistic exists for South Carolina: settlements are confidential, verdicts are a tiny unrepresentative sample, and the range across cases spans from a few thousand dollars to many millions. A number that averages a bruised knee and a traumatic brain injury tells you nothing about your case. Anyone who quotes you a value before reading your records is guessing, or selling.</p>'
       + '<h2>How we give you a number</h2>'
       + steps([
           ("Not at the first call.", " We will tell you whether the claim is worth pursuing and roughly what category it falls in."),
           ("When treatment is done, or the prognosis is clear.", " We gather every bill and record, the wage documentation, and the doctor's opinion on the future, and we identify every policy."),
           ("Then a range, in writing.", " With the reasoning: what the insurer will argue, what the evidence answers, and what a jury in this county has done with comparable injuries."),
           ("Then a demand.", " Higher than the range, documented, with a deadline. Negotiation follows, and suit if it stalls."),
       ])
       + '<h2>What the contingency fee means for your number</h2>'
       + '<p>The fee is a percentage of the recovery, and case costs come out of it too, as the engagement agreement explains in writing. What matters is what you keep, and the studies insurers themselves have run show that represented claimants keep more after fees than unrepresented ones on comparable injuries, because the recovery is larger. We will tell you when that is not true for your case, and it sometimes is not.</p>'
       + asked("reddit_charleston_accidents", "reddit_legaladvice_sc", "reddit_insurance_sc", "justia_sc_injury")
       + callout("<b>Frost first:</b> the insurer's first offer is a number chosen to be accepted by someone who does not know what the claim is worth. Find out before you answer it.")
   ),
   faqs=[
       ("What is the average car accident settlement in South Carolina?", "There is no reliable average. Settlements are confidential and range from a few thousand dollars to millions depending on the injury, the treatment, fault and the insurance available. Published averages are marketing."),
       ("How is pain and suffering calculated in South Carolina?", "There is no formula in South Carolina law. Insurers use internal software; juries use judgment. In practice it is argued from the medical record, the duration and permanence of the injury, and its effect on daily life."),
       ("Does South Carolina cap car accident damages?", "Not for ordinary injury claims. Caps apply to claims against government entities and to punitive damages (with exceptions, including impaired drivers)."),
       ("Will I get more money with a lawyer?", "Usually, after the fee, on injury claims with real medical treatment. Not always on small property claims, and we will tell you which yours is."),
   ],
   sources=[("S.C. Code Title 15, Chapter 32 (damages)", "https://www.scstatehouse.gov/code/t15c032.php", False), ("S.C. Code § 15-38-15 (apportionment)", "https://www.scstatehouse.gov/code/t15c038.php", False)],
   related=[HUB + "/how-long-does-a-car-accident-case-take", HUB + "/south-carolina-comparative-negligence", HUB + "/uninsured-motorist-accidents"])

# ----------------------------------------------------------------------------- 9. Timeline
sp(HUB + "/how-long-does-a-car-accident-case-take",
   title="How Long Does a Car Accident Case Take in South Carolina? | Timeline",
   description="A realistic timeline for a South Carolina car accident claim, from the crash to the check: treatment, the demand, negotiation, when a lawsuit is filed, mediation, and trial in Dorchester, Berkeley or Charleston County. What speeds a case up and what slows it down.",
   h1="How long does a car accident case take in South Carolina?",
   summary="From crash to check: treatment, demand, negotiation, lawsuit, mediation and trial, with realistic timeframes for the tri-county courts.",
   lead="Months for most claims, one to two years when a lawsuit is needed. Here is what happens in each stage and why the calendar looks the way it does.",
   body=(
       answer("Most South Carolina car accident injury claims resolve in six to twelve months: the time it takes to finish treatment (or reach a clear prognosis), assemble the records, send a demand, and negotiate. Claims that require a lawsuit typically take twelve to twenty-four months from filing to resolution in Dorchester, Berkeley or Charleston County, with most settling at or after mediation rather than at trial. The single largest factor is medical: a claim should not settle before the injury's course is known, because the settlement is final.")
       + '<h2>The stages</h2>'
       + table(["Stage", "What happens", "Typical time"], [
           ["Weeks 1 to 2", "Report the crash, open claims, preserve evidence, get medical care, retain counsel", "Days"],
           ["Treatment", "Follow the treatment plan until you recover or your doctor says you have reached maximum medical improvement (MMI)", "Weeks to many months, depending on the injury"],
           ["Records and demand", "Gather every bill, record and wage document; identify every policy; write the demand package", "3 to 6 weeks after treatment ends"],
           ["Insurer review and negotiation", "The insurer evaluates, responds (often with a low offer), and the parties negotiate", "30 to 90 days"],
           ["Lawsuit filed", "If the insurer will not pay fair value, suit is filed in the county where the crash happened", "Must be within 3 years of the crash"],
           ["Discovery", "Written questions, document exchange, depositions of the parties, doctors and witnesses", "6 to 12 months"],
           ["Mediation", "Required before trial in the tri-county courts; a neutral mediator works both sides toward a number. Most cases settle here", "Usually 9 to 15 months after filing"],
           ["Trial", "A jury decides fault and damages", "12 to 24 months after filing, depending on the county's docket"],
       ])
       + '<h2>What slows a case down</h2>'
       + checks([
           "<b>Ongoing treatment.</b> The good kind of slow. A claim settled before surgery is a claim that paid for nothing.",
           "<b>Disputed fault.</b> When the insurer denies liability, the claim often needs a lawsuit to force the evidence out.",
           "<b>Low policy limits and UM/UIM claims.</b> Two or three insurers instead of one, each with its own consent and evaluation steps.",
           "<b>Liens.</b> Medicare in particular can take months to state its reimbursement figure.",
           "<b>Court dockets.</b> Charleston County's civil docket is the busiest of the three; Dorchester and Berkeley move somewhat faster.",
       ])
       + '<h2>What speeds it up</h2>'
       + checks([
           "Same-day medical care and a consistent treatment record, so the injury is documented from the start.",
           "Evidence gathered in the first weeks, so fault is not seriously disputable.",
           "Clear policy limits and prompt policy-limits demands when the injury obviously exceeds them.",
           "A firm the insurer knows will file suit and try the case. Insurers move faster for lawyers who do.",
       ])
       + '<h2>Getting money sooner</h2>'
       + '<p>While the claim is open: MedPay coverage pays medical bills quickly; the property-damage claim can be settled separately and early; disability coverage at work may apply; and in some cases a partial payment can be negotiated. What we do not recommend is pre-settlement “lawsuit loans,” whose interest rates consume settlements. Ask us before signing one.</p>'
       + '<h2>Why we will not rush yours</h2>'
       + f'<p>A settlement is final. If you settle in month three and need an injection in month five, the injection is yours to pay. The insurer knows this, which is why the early offer comes early. We move every case as fast as the medicine allows and no faster. {A(HUB + "/how-much-is-my-car-accident-case-worth", "How the value is determined")}.</p>'
       + asked("reddit_charleston_accidents", "reddit_legaladvice_sc", "justia_sc_injury", "avvo_sc_car")
       + callout("<b>Frost first:</b> if an insurer tells you a claim will “take years” with a lawyer and “settle today” without one, the second half is true and it is the problem.")
   ),
   faqs=[
       ("How long does an insurance company have to settle a claim in South Carolina?", "There is no fixed deadline to settle, but South Carolina requires insurers to handle claims in good faith and to respond reasonably. Unreasonable delay or denial can support a bad-faith claim against your own insurer."),
       ("Do most car accident cases go to trial?", "No. The large majority settle, most often at or after mediation. Preparing every case for trial is what makes settlement happen."),
       ("How long after a demand letter does settlement take?", "Typically 30 to 90 days for the insurer's evaluation and the negotiation that follows. Longer if fault or the medicine is disputed."),
       ("Can I settle my property damage claim before my injury claim?", "Yes, and you usually should. Read the release to be sure it covers only the vehicle."),
   ],
   sources=[("S.C. Code § 15-3-530 (three-year limitations period)", "https://www.scstatehouse.gov/code/t15c003.php", False)],
   related=[HUB + "/how-much-is-my-car-accident-case-worth", HUB + "/south-carolina-car-accident-statute-of-limitations", HUB + "/should-i-talk-to-the-other-drivers-insurance-company"])

# ----------------------------------------------------------------------------- QUESTIONS HUB
questions_body = (
    '<p class="lead">Every question answered on this site, in one place, grouped by topic, each with a link to the page that explains it fully. These are the questions people type into Google, ask on Reddit and Nextdoor, and post on legal Q&amp;A boards after a crash or an injury in the Lowcountry. The answers are South Carolina law, written by the attorney who handles these cases.</p>'
    '<h2>Where these questions get asked</h2>'
    '<p>We read the same threads you do. Other drivers\' experiences are useful; their legal conclusions are often from another state. Here is where the conversation happens, and where you can see the questions in their own words:</p>'
    + ul([link(k) for k in ("reddit_charleston_accidents", "reddit_charleston_lawyer", "reddit_summerville_accidents", "reddit_southcarolina_accidents", "reddit_legaladvice_sc", "reddit_insurance_sc", "reddit_charleston_dogbite", "nextdoor_summerville", "nextdoor_goose_creek", "justia_sc_car", "justia_sc_injury", "justia_sc_dog", "avvo_sc_car", "scdoi_faq")])
    + '<p>If your question is not here, ask it. The call is free, and it may become the next page.</p>'
    + '[[allfaqs]]'
    + '<h2>Ask your question</h2><p>Tell us what happened. We answer the same day.</p>[[form]]'
    + band("Still have a question?", "Call and ask it. The consultation is free, and you will get a straight answer.")
)
page("questions", kind="page", layout="one",
     title="Questions Summerville Drivers Ask After a Crash | Answered by an Attorney",
     description="Every question answered on this site, in one place: after a crash, dog bite, fall or work injury in Summerville and the Lowcountry. South Carolina law, in plain English, with links to where people ask.",
     h1="Questions people ask after a crash or an injury", eyebrow="Answered by a Summerville injury attorney", nav_label="Questions people ask",
     lead="The questions from Google, Reddit, Nextdoor and the legal Q&A boards, answered for South Carolina.",
     summary="Every question on the site, in one place.", body=questions_body, priority=0.8, changefreq="weekly")
