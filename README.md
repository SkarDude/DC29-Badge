# DC29-Badge

Scripts, notes, shoutouts and completion of the Defcon 29 Badge

- [DC29-Badge](#dc29-badge)
  - [DefCon 29 General](#defcon-29-general)
  - [ReCon (see what I did there)](#recon-see-what-i-did-there)
  - [Tinkering](#tinkering)
  - [Part 1](#part-1)
  - [Part 2](#part-2)
  - [Part 3](#part-3)
  - [Part 4](#part-4)
  - [Part 5](#part-5)
  - [Part 6](#part-6)
  - [Part 7](#part-7)
  - [Part 8](#part-8)
  - [Part 9](#part-9)
  - [Part 10](#part-10)
  - [Part 11](#part-11)
  - [Part 12](#part-12)
  - [Part 13](#part-13)
  - [Summary](#summary)

## DefCon 29 General

This year the conference was a little different with it being a hybrid con. There was not as much to do in person. So it allowed [Vincent Wingfield](https://www.linkedin.com/in/vincentwingfield/) (electrical engineer) and myself [Alex Hough](https://alexpert.tech) (software dev) to focus on the badge challenge.

## ReCon (see what I did there)

Images of the badge leaked online early and we were very excited to see a physical, social, and hackeresque badge. Recognizing the i/o ports as usb c / a. I ordered every cable possible as well as some rechargeable Li-Ion 2032 battery. I also decided to pack a burner laptop (kali), gl-inet mango, and some other tinkering tools. My buddy being more hardware oriented packed a breadboard, jumper wires, multimeter, basically everything short of the oscope and solder iron.

## Tinkering

We didn't officially sit down and mess with the badge till about 13:00 on Aug 5th. We took advantage of blackhat being offered and grabbed some swag / knowledge. After getting the badge assembled and turned on it did nothing but flash rainbow for a brief second. Loved the clickiness and the cleverness of the lanyard being a UsbA->C. Now the tinkering begins:
1. All the plugins
   * Single badge UsbA <-> UsbC (Green, red, yellow, blue flashing at us)
   * Dual badge UsbA <-> UsbA (nothing)
   * Dual badge UsbC <-> UsbC (nothing)
   * Dual badge UsbA <-> UsbC (noises and buttons lighting up on one badge)
   * Dual cable/badge UsbA <-> UsbC (one badge spazzing an led clearly us bricking something)
   * Dual badge Male <-> Female "signal" port (both badges lit up)
   * Back to dual badge UsbA <-> UsbC (we slow down and realize this initiates a game one badge master had a green button press to start the game, Simon)
2. Badge buttons
   * Button smashing (nothing)
   * Konami code attempt (nothing)
   * PCB has text Pro tip 3,2,1 so tried button pressing in that order (nothing)
   * RTFM (yes it took us this long to read the manual) defcon.org/signal
     * Holding down bottom right button 4 LED blinking red storage mount mode
   * Quickly tested holding down other buttons
     * Holding down button 1 Green starts single player Simon
3. Hardware
   * Multimeter on the back of the badge for the exposed points
   * Recognized the pads on the back were either ground or positive (useful for later)
   * Bridged pads temporarily (no badge action)
   * Bridged points temporarily (no badge action)
4. Graphics
   * Started trying to decode binary on back of the badge. I recognized characters were grouping of 8 vertically spelt (RED)
   * We started identifying the graphics from sci fi movies or points in history
    * I went down a rabbit hole of thinking the graphics shorthand would unscramble to something (nothing)
      * RED
      * ET
      * MAX
      * 41
      * MIB
   * Inspected the lanyard for clues on the tape measure lanyard "29" lined up with green (nothing really here, maybe to start simon but nothing else)
5. Connected to the computer
   * My volume kept changing realized the far right is a slider input neat!
   * Buttons interacted with the computer in different ways also cool
   * Put it in mount mode saw it as storage (we had latest f/w already)
   * Turned badge off and connected via screen
    * Got a prompt with badge stats
6. Games
   * For some reason after we saw the stats we thought we needed to get to 29 levels in simon to get the next Part
      * Multiple badge we got to 16, and single badge my buddy got to 35 it did not do anything in the terminal just updated our stats
7. Discord
   * Users were spamming 32 char keys and I realized that is how virtual badges connected we both had 1 human at that point from our Signal connection earlier
   * Instead of meeting people we decided to attack the virtual route

## Part 1

I did not realize Part 1 was connecting with all the different badge types at first I just thought it was connecting to 20 badges. I saw a badge bot was shared in discord a tinkerer was scraping badge data and sharing it in an IRC chat to complete this in an automated fashion!
* https://rossmarks.uk/git/0xRM/DC29BadgeBot
  * I decided to get involved and got a hat tip as a contributor for linux issues
  * Went to the gym while badge bot was running came back and We Had The signal
  * Url was shared in badge presentation cool exposure

## Part 2

The terminal prompt showed me once we had the signal all badge types now we needed to share our signal with 20 badges. Badge Bot did not have enough users yet to allow us to complete this Part. We went to discord chat and started spamming and replying like everyone else.
* Discord 32 char key spamming / replies
  * Fun way to interact with people
  * Most people were honest and replied quickly
    * copy/pasta was tedious on linux terminal <-> discord (4,5)
  * Discord went down at bally's rate limited (I had a repeater w/ vpn)
    * Luckily my burner had hotspot data
  * Finally we both got to 20 probably around 01:00

## [Part 3](https://defcon.org/signal/WhatIfIToldYou/)

Once we shared the signal a URL was spit out /WhatIfIToldYou and I realized it needed to be appended to /signal/ (thanks previous web based CTF). Classic matrix prompt Red or Blue pill. We new the back of the badge decoded to Red but nothing stood out to us immediately there. My buddy mentioned what if they meant a physical disconnect and I brushed it off. Attempts:
1. Terminal Connection
   * Saw you could change LED color of Buttons
      * Changed all 4 to Red (nothing)
      * Changed all 4 to Blue (nothing)
      * Remembered the PCB pro tip changed 3 to red or 3 to blue (nothing)
      * Went to sleep
2. Physical hardware
   * After waking up we looked over the badge and recognized the pad coming out of Red binary on the wire did not look like the bottom "disconnected" pad
   * We pulled out the knife and cut the pad (nothing changed on badge bootup)
   * Hooked up to the computer and we got a new URL for the challenge (this is when it clicked the terminal is the controller for the badge challenge as well as the urls)

## [Part 4](https://defcon.org/signal/YourJourneyBegins/)

We were so excited for the challenge. First glance it appaeared to be a cypher. Checking the html revealed a hint that is easy. My cryptography class prepared me to do this by hand but I used dcode.fr and assumed it was a caesar-cipher. It translated to a message how this was easy but do not expect them all to to be this easy and gave us the next url which is a synonym for Caeser Cipher neat.

## [Part 5](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/)

Prompt was a poem and the hint in the html was nothing lasts forever. We repeated it multiple times nothing was clicking. Neither of us are DefCon history buffs, so I went over to Wikipedia and noticed the con was hosted at other hotels previously. Some of the hotels exist but some I have never heard of and when I googled them I realized they were demolished etc. "We won't forget the ones we lost". Sands and Aladdin yes we got it well appending that to the url did nothing 404. Further google foo showed that Sahara was also technically demolished at least where the con was held. In order /sandssaharaaladdin (nothing). WTH my buddy realized all the other previous urls were title case /SandsSaharaAladdin it worked!!!

## [Part 6](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/)

Picture of a chip and the chip shortage and the title of the page was Bet You Can't Eat Just One the message was clear we needed to find the IC that was used in previous badges and which one was used twice. We originally tried the chip that was used on the DC29 badge but it did not workout. Google foo was not working at first here. No hint in html but now we realized the picture name, and title of the pages are also hints going forward. Upped the ante on my google foo and searched defcon "badge" + "presentations" and a few stood out but "A Five-Year History of Electronic Badges" By kingpin stood out the most. Scouring the pages of the presentation we recognized two of the badges used the same chip and typed that in it did not work 17/18. My EE buddy was reading a schematic from the presentation and realized it needed the VLC appended to it.

## [Part 7](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/)

This step launched a gif with no text and no hints in the hmtl. The title was 1 2 4 and the image name was jennytones.gif.

1. HTML Scouring
    * Since generally there was hints in the html I was checking all of the rest of the HTML of the page for any clues. Maybe clues hidden in color choices which was just black for background.
    * Text color was set which was odd to me it was set to white but there was no text so I tried /white (nothing)
2. Title of page was 1 2 4
   * Maybe this has to do with that pcb message 1, 2, 3
     * Tried all different aspects /3,/123,/124,/4 (nothing)
   * Pressed different buttons while plugged into computer and into a friends badge (nothing)
3. Noticed different aspects of the image changed colors over time .gif
    1. Wrote down the changes in the image screenshotted etc.
    2. Since the image was the focus maybe the clue was in the exif data (nothing)
    3. Being a .gif maybe there is something hiding inside used binwalk to extract (nothing)
    4. Small steganography rabbit hole but nothing was hiding in plain site
    5. Went to sleep
4. Upon waking up we needed a hint we searched discord for "jenny".
    * Saw similar steganography approaches but nothing concrete
    * Saw 8675309, (guess I am uncultured forgot about the jenny song)
5. 8675309
    * This had to be it title of image was jennytones, and the title of the page was numbers that fit around the iconic phone number /8675309 did not work
    * It took another discord leak for us to get moving apparently the virtual badge presentation showed a different image of the internals then the physical badge presentation we attended.
    * If you looked at the right angle next to the USB A port there was a roman numeral humans were 3 which did not stand out.
    * My buddy ran downstairs for a talk and got a glimpse of a goon badge 9 and a vendor 8. Which cut down on us brute forcing the entire thing
6. [Jenny Python Script](jenny.py)
    * Even though we figured out a few of the placements I was not about to try all the urls by hand (4! = 28)
    * Generated a quick script that would plug in the rest of the places
      * Tried to use requests library to just return the url that returned 200 but defcon.org was not cooperating
      * Manually cmd + clicked 28 urls till we got it luckily it was towards the top

## [Part 8](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/VendorSpeakerArtistCreatorHumanPressGoon/)

Hackers have disabled our broadcast. Don't let them stop the signal. Luckily we recognized the back of the badge TV's from earlier and the Max Headroom incident. I mentioned we probably need to connect the disconnected pad at the bottom my hardware buddy disagreed :p.

1. We brute forced a couple urls /Max /MaxHeadroom /Chicago /WGNTV /WTTW etc. (deadend)
2. Back to physical yay, we didn't want to solder our board just yet and jumper wires (taped or manually held) was not doing anything to the badge or in the terminal
3. I mentioned we should try a pencil (graphite conductor thanks HS robotics) to fill in the pad and we went downstairs and grabbed one from the front desk.
   1. Filled in nothing physical happened
   2. Ran back up and plugged into computer we got the next url!

## [Part 9](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/VendorSpeakerArtistCreatorHumanPressGoon/WatchYourHead)

Another encoded message tried caeser cipher it did not work brute forcing. Checked html comment for hint `ivtrarer` did some google foo on this and figured out it was a vigenere cipher. I recognized some of the words were 3 letters so either the, you etc. I tested the cipher as a known word with an unknown key in dcode.fr and figured out the key was DEFCON and got the message. The title of the page was Reminiscing and the message refers back to defcon history. So the whole time we were tinkering in our hotel room we were watching DefCon TV on the hotel TV and we learned that AlexisPark is known as a place many hackers enjoyed. They still steal the front entrance rug, and kids were allowed since it wasnt a casino. It immediately clicked for my buddy that the next clue was /AlexisPark. Great timing we got a DefCon history talk on DCTV

## [Part 10](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/VendorSpeakerArtistCreatorHumanPressGoon/WatchYourHead/AlexisPark/)

Next challenge prompted us with a string of numbers and a title Named After and the image name was cipher.png. Having some experience in graphing calculator programming specifically mapping a button press to an integer I realized we were looking at some sort of input mapper or char map. Some google foo and we found an ASCII decoder and did the decoding by hand with me reading the numbers and my buddy decoding. This revealed a message about the badge making process luckily we watched the in person badge conference and new they named their Resin Printers and Vats we just forgot the names. We found the virtual recorded talk and fast forwarded to the part they talk about the vats. Some brute forcing happened on the names but it was just the name of the movie SnowWhiteAndTheSevenDwarfs the prince charming was left out of the naming for the url.

## [Part 11](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/VendorSpeakerArtistCreatorHumanPressGoon/WatchYourHead/AlexisPark/SnowWhiteAndTheSevenDwarfs/)

We were shown a meme that more commonly reads "Aliens" but it said connections by this point we knew this was the other 2 silver pads on the badge between ET finger and the alien ship. Nothing happened on the badge when we bridged we realized we had to be on the terminal. My buddy held very still on the connections while I plugged into the terminal. It took a few tries but we got the next url (I still have not soldered my badge)

## [Part 12](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/VendorSpeakerArtistCreatorHumanPressGoon/WatchYourHead/AlexisPark/SnowWhiteAndTheSevenDwarfs/ItWasTotallyAliens/)

We had a message about the encryption on the badge to generate those virtual strings. Being in the IOT world now I thought the clue was RNG but it was not. I just googled common obfuscation for microcontrollers and XOR showed up regularly and that just happened to be the next URL.

## [Part 13](https://defcon.org/signal/YourJourneyBegins/AlphabetShift/SandsSaharaAladdin/MC56F8006VLC/VendorSpeakerArtistCreatorHumanPressGoon/WatchYourHead/AlexisPark/SnowWhiteAndTheSevenDwarfs/ItWasTotallyAliens/XOR/)

We are shown a picture of an older paper with dates. Then a string of hyphen separated numbers with 5 places instead of 3 as shown in the photo. I recognized the photo but it took me a bit to realize it was a photo from national treasure. The hint was kind of useful in the html it was Year - P -L -W -L. While we were trying to figure out what it was referring to I recognized that the years never went above 27 which made me think of previous def cons. It also clicked finally that it was national treasure and we started watching clips on youtube with the lemons and after (why does the dad have so  many lemons in his fridge). We finally got the clue it was an Ottendorf cipher or a book cipher. So Year - page - line - word - letter for 73 chars yikes. Knowing that the year linked to the programs as the 28/safe mode did not have one and 29 was not available yet we had to pull up all of the pdfs. Hat tip to my buddy for massaging and decoding this by hand while I played craps that night. Ultimately with some fine tweaking we had the challenge done at 04:00 on Aug 7. We definitely were not first but we had a blast.

## Summary

DefCon 29 was fun but different. We focused on the badge and getting it completed. Thank you MK Factor and everyone else involved in getting the badge together. This was my favorite part of DefCon this year and was a lot of fun to solve. Hopefully next year my buddy and I can join a larger team so maybe we can finish first :D
