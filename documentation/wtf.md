# YERP!... WTF? Some info on what this is and why it's being developed

## Some Background 

YERP! - Your Emergency Response Platform - exists under the context of a drug prohibiton pandemic. Under which 100,306 people died from drug overdose from April 2020-April 2021 in the US alone. Many of these deaths are from opioid overdose, with opioids detected as [present in 70.6% of overdoses in 2019](https://www.cdc.gov/drugoverdose/deaths/index.html).

As someone who's lost friends to such circumstances, around 2018 I found myself  increasingly involved in [harm reduction](https://harmreduction.org), a movement which seeks to safeguard long-term livelihood and autonomy for people subject to harms such  as drug criminalization, drug prohibition, and the unregulated and increasingly dangerous supply [these conditions encourage](https://filtermag.org/infographic-the-iron-law-of-prohibition/)--while also addressing immediate needs for safety and well-being these situations necessitate.

One of these needs is quick and effective intervention against accidental drug overdose, [often via naloxone](https://harmreduction.org/issues/overdose-prevention/overview/overdose-basics/understanding-naloxone/), and/or rescue breathing and other forms of oxygenation. But due to the way that opioid overdose occurs, with consciousness being lost during the process, it's impossible for someone to self-administer naloxone.

This is why a harm reduction approach to using drugs suggests using around others--especially others equipped with naloxone and the knowledge of how to use it. This is sometimes referred to as **spotting**. A slogan often comes up in harm reduction to address this: **never use alone** (it's also the name of [a wonderful, free service for spotting over the phone](https://neverusealone.org)).

However, this is also a contradiction with the principles of harm reduction, which seeks to provide support in de-stigmatizing *every* and *any* method of drug use one would intentionally partake in. And as [Philadelphia's Project SAFE has expertly gathered](https://www.vitalstrategies.org/wp-content/uploads/PWUD-ServiceProvider-Guide-07142021.pdf), solo use often ends up occuring due to other even more immediate risks. 

YERP! exists as one effort amongst many to address this contradiction.

***Some additional vital background, to work in here:***

The Kensington neighborhood in North Philadelphia has in recent years been a site for multiple Hepatitis-A outbreaks. These outbreaks commonly happen when communal sanitation is lacking. And as a community with both a large unhoused population and a large open-air drug market, public bathroom use is often restricted. This seems due in part to general biases against unhoused people and people who use drugs, though the circumstances of providing bathroom access even for those well-intentioned towards community needs are often under-equipped to do so.

"Smart spotting" via systems like YERP! may be one way to enable increased bathroom access.  Which in turn stands to improve public sanitation and public health, along with doing better to meet needs of dignity and privacy usually left underserved for unhoused populations.

## Other Similar Projects
### (Some Shoulders On Which to Stand)

In the Spring of 2019, Philadelphia housing-first organization enlisted a New Hampshire-based company called LifeSaver Alert, LLC to install overdose detection systems in their bathrooms, [as covered by Filter](https://filtermag.org/how-technology-is-rapidly-advancing-overdose-resistant-bathrooms/) and talked about across the Philadelphia harm reduction community.

As an organizer with the Philadelphia Drug Users' Union at the time, this came onto my radar as a novel and interesting approach. Though, as well, fraught with a number of setbacks. These systems begin their monitoring process every time a bathroom door is closed, which requires facilities to keep their bathroom doors open when not in use. Commonly recurring false positives (such as getting sucked into social media while sitting on the toilet, being still enough that a PIR sensor doesn't detect any movement). These false positives would, like true positives, trigger a fire alarm-volume siren and strobe light. These systems were also hand-built, proprietary, and seemed like they'd be difficult to afford for many instances in which this sort of spotting would be useful.

This led me to research other options for similar interventions, such as [Brave Co-Op](https://brave.coop)'s [Brave Sensor](https://github.com/bravetechnologycoop/BraveSensor). This was, and is an open source project put together by a co-op run on the same principles that dictate the services they provide (both of which I'm still amazed and inspired by).

## Where YERP! Comes In

Both Brave's sensors and LifeAlert's systems are made to address specific sets of needs. YERP! doesn't seek to compete with these options, but rather to work towards shared goals: providing safer accommodations to those who need them. *In collaboration with* those who need them. 

And thanks to being build on top of incredibly modular and adaptable software, YERP! is in turn modular and adaptable as well. Variations and customizations of installations are encouraged and welcomed. In the coming weeks and months we'll be detailing options for implementation outside of the stock installation, including options for:

- Installations catering towards various accessibility needs such as impairment with movement, vision, and hearing 
- Battery-operated popup installations, running offline or online
- Installations for home use, service providers, retail stores, and nightlife venues

Implementation in real-life settings for testing and practical use are forthcoming. Anyone interested helping with this testing are invited to implement the code and instructions in this repo as you see fit; our sponsor organization, Philadelphia-based [Cool Industries](https://cool.industries) can also be available for installation, implementation and maintenance.