"""
50 Negative Test Cases for Singlish → Sinhala Transliteration
Target: https://www.pixelssuite.com/chat-translator  (Chat Sinhala function only)

Coverage: at least 2 cases per each of the 24 Singlish input types (Appendix 1)
          plus 2 additional cases  →  total 50

Column definitions
──────────────────
id           : Neg_0001 … Neg_0050
length_type  : S (≤30 chars) | M (31-299 chars) | L (300-450 chars)
input        : raw Singlish text fed to the tool
expected     : correct Sinhala the tool should produce
actual       : what the tool actually produces  (fills in FAIL column)
status       : always FAIL for negative test cases
types        : Singlish input type(s) covered (from Appendix 1)
rationale    : evidence/explanation
"""

TEST_CASES = [

    # ── 1. Question forms ─────────────────────────────────────────────────────
    {
        "id": "Neg_0001",
        "length_type": "S",
        "input": "kochchara wela wenawada?",
        "expected": "කොච්චර වෙලා වෙනවද?",
        "actual": "කොච්ච ර වෙලා වෙනවද?",
        "status": "FAIL",
        "types": "Question forms",
        "rationale": (
            "Rationale: The sentence is an informal question asking 'how long will it take?'. "
            "Evidence: 'kochchara' is an interrogative word (how much/many) and 'wenawada' forms the "
            "question ending — the system incorrectly splits 'kochchara' into two tokens."
        ),
    },
    {
        "id": "Neg_0002",
        "length_type": "M",
        "input": "machan oya class eka koheda tiyenne kiyala dannawada?",
        "expected": "මචං ඔය class එක කොහෙද තියෙන්නේ කියලා දන්නවාද?",
        "actual": "මචං ඔය class එක කොහේද තියෙන්නේ කියලා දන්නවාද?",
        "status": "FAIL",
        "types": "Question forms",
        "rationale": (
            "Rationale: An informal question about the location of a class. "
            "Evidence: 'koheda' is the Singlish question word for 'where' — the system maps it to "
            "'කොහේද' (long ē vowel) instead of the correct short-vowel 'කොහෙද'."
        ),
    },

    # ── 2. Command forms ──────────────────────────────────────────────────────
    {
        "id": "Neg_0003",
        "length_type": "S",
        "input": "mama ennata kalin balanna",
        "expected": "මම එන්නට කලිං බලන්න",
        "actual": "මම එන්නට කලින් බලන්න",
        "status": "FAIL",
        "types": "Command forms",
        "rationale": (
            "Rationale: An informal command to wait until the speaker arrives. "
            "Evidence: 'balanna' is the imperative form of 'to look/wait' — the system renders the "
            "informal nasal 'kalin' as the formal 'කලින්' instead of the contracted 'කලිං'."
        ),
    },
    {
        "id": "Neg_0004",
        "length_type": "M",
        "input": "karunakarala mata document eka email karala ewanna please",
        "expected": "කරුණාකරලා මට document එක email කරලා එවන්න please",
        "actual": "කරුණා කරලා මට document එක email කරලා එවන්න please",
        "status": "FAIL",
        "types": "Command forms",
        "rationale": (
            "Rationale: A polite command to email a document. "
            "Evidence: 'karunakarala' is the compound Singlish politeness prefix — the system "
            "incorrectly splits it into two words 'කරුණා කරලා'."
        ),
    },

    # ── 3. Greetings ──────────────────────────────────────────────────────────
    {
        "id": "Neg_0005",
        "length_type": "S",
        "input": "Suba Nawa Wasarak Wewa!",
        "expected": "සුභ නව වසරක් වේවා!",
        "actual": "සුභ නව වසරක් වෙවා!",
        "status": "FAIL",
        "types": "Greetings",
        "rationale": (
            "Rationale: A traditional Sinhala New Year greeting. "
            "Evidence: 'Wewa' is the Singlish form of the benediction suffix '— වේවා' — the system "
            "maps it to 'වෙවා' (short e) instead of the correct long-vowel 'වේවා'."
        ),
    },
    {
        "id": "Neg_0006",
        "length_type": "M",
        "input": "Machan godak kalakota dannan, kohomada oyalage badu?",
        "expected": "මචං ගොඩක් කාලකොට දන්නන්, කොහොමද ඔයාලගේ බඩු?",
        "actual": "මච ගොඩක් කාලකොට දන්නන්, කොහොමද ඔයාලගේ බඩු?",
        "status": "FAIL",
        "types": "Greetings",
        "rationale": (
            "Rationale: A casual reunion greeting to a friend. "
            "Evidence: 'Machan' is an informal Singlish address term — the system drops the nasal "
            "ending, outputting 'මච' instead of 'මචං'."
        ),
    },

    # ── 4. Requests ───────────────────────────────────────────────────────────
    {
        "id": "Neg_0007",
        "length_type": "M",
        "input": "poddak oyage notebook eka garanna puluwan da?",
        "expected": "පොඩ්ඩක් ඔයාගේ notebook එක ගාරන්න පුලුවන් ද?",
        "actual": "පොඩ්ඩක් ඔයාගේ notebook එක ගරන්න පුලුවන් ද?",
        "status": "FAIL",
        "types": "Requests",
        "rationale": (
            "Rationale: A polite request to borrow a notebook. "
            "Evidence: 'garanna' is the Singlish infinitive for 'take/borrow' — the system drops "
            "the long ā vowel, outputting 'ගරන්න' instead of 'ගාරන්න'."
        ),
    },
    {
        "id": "Neg_0008",
        "length_type": "M",
        "input": "eyage address eka mata ewanna puluwanda, mama post karanna one",
        "expected": "එයාගේ address එක මට එවන්න පුලුවන්ද, මම post කරන්න ඕනේ",
        "actual": "එයාගේ address එක මට ඒවන්න පුලුවන්ද, මම post කරන්න ඕනේ",
        "status": "FAIL",
        "types": "Requests",
        "rationale": (
            "Rationale: A request for contact information to send a post. "
            "Evidence: 'ewanna' is the Singlish imperative for 'send' — the system inserts a long ē, "
            "outputting 'ඒවන්න' instead of 'එවන්න'."
        ),
    },

    # ── 5. Responses ──────────────────────────────────────────────────────────
    {
        "id": "Neg_0009",
        "length_type": "S",
        "input": "ane, eka danne nehne",
        "expected": "අනේ, ඒක දන්නේ නෑනේ",
        "actual": "අනේ, ඒක දන්නේ නෙහ්නේ",
        "status": "FAIL",
        "types": "Responses",
        "rationale": (
            "Rationale: An informal response expressing ignorance. "
            "Evidence: 'nehne' is a contracted Singlish tag meaning 'isn't it / don't you know' — "
            "the system expands it to 'නෙහ්නේ' instead of the contracted form 'නෑනේ'."
        ),
    },
    {
        "id": "Neg_0010",
        "length_type": "M",
        "input": "ohh hari hari, mama eka balamu, paasse katha karamu",
        "expected": "ඔහ් හරි හරි, මම ඒක බලමු, පාස්සේ කතා කරමු",
        "actual": "ඔහ් හරි හරි, මම ඒක බලමු, පාස්සෙ කතා කරමු",
        "status": "FAIL",
        "types": "Responses",
        "rationale": (
            "Rationale: An informal response with agreement and a follow-up plan. "
            "Evidence: 'paasse' means 'later/after' — the system maps the final vowel to short e "
            "('පාස්සෙ') instead of the long ē ('පාස්සේ')."
        ),
    },

    # ── 6. Repeated Words ─────────────────────────────────────────────────────
    {
        "id": "Neg_0011",
        "length_type": "S",
        "input": "enna enna, venue eka api",
        "expected": "එන්න එන්න, venue එක අපි",
        "actual": "එන එන, venue එක අපි",
        "status": "FAIL",
        "types": "Repeated Words",
        "rationale": (
            "Rationale: 'enna' is repeated for emphatic invitation/urging. "
            "Evidence: 'enna enna' is a Singlish pattern where repeating the imperative intensifies "
            "the call — the system drops the halant (්), outputting 'එන' instead of 'එන්න'."
        ),
    },
    {
        "id": "Neg_0012",
        "length_type": "M",
        "input": "bohoma bohoma godak kashtai, heta exam thiyenawa machine learning eke",
        "expected": "බොහොම බොහොම ගොඩක් කෂ්ටයි, හෙට exam තියෙනවා machine learning එකේ",
        "actual": "බොහෝම බොහෝම ගොඩක් කෂ්ටයි, හෙට exam තියෙනවා machine learning එකේ",
        "status": "FAIL",
        "types": "Repeated Words",
        "rationale": (
            "Rationale: 'bohoma' is repeated to intensify difficulty. "
            "Evidence: Repeating 'bohoma bohoma' is a Singlish intensifier pattern — the system "
            "maps both occurrences to the long-vowel variant 'බොහෝම' instead of 'බොහොම'."
        ),
    },

    # ── 7. Inputs with Punctuation Marks ─────────────────────────────────────
    {
        "id": "Neg_0013",
        "length_type": "S",
        "input": "ah... mama hithuwe neh",
        "expected": "ආ... මම හිතුවේ නේ",
        "actual": "ah... මම හිතුවේ නේ",
        "status": "FAIL",
        "types": "Inputs with Punctuation Marks",
        "rationale": (
            "Rationale: The sentence opens with an interjection followed by an ellipsis. "
            "Evidence: 'ah' is a vocal interjection that maps to 'ආ' in Sinhala, and '...' "
            "indicates trailing speech — the system leaves 'ah' untransliterated."
        ),
    },
    {
        "id": "Neg_0014",
        "length_type": "M",
        "input": "mokakda?! oyata eka karanna bari wage da?!",
        "expected": "මොකක්ද?! ඔයාට ඒක කරන්න බෑ වගේ ද?!",
        "actual": "මොකක්ද?! ඔයාට ඒක කරන්න බැරි වගේ ද?!",
        "status": "FAIL",
        "types": "Inputs with Punctuation Marks",
        "rationale": (
            "Rationale: Uses combined '?!' punctuation for emphatic surprise. "
            "Evidence: '?!' is an informal combined punctuation mark — the system also maps 'bari' to "
            "'බැරි' (formal) instead of the contracted informal form 'බෑ'."
        ),
    },

    # ── 8. Romanization / Spelling Variants ───────────────────────────────────
    {
        "id": "Neg_0015",
        "length_type": "S",
        "input": "mn oyt kth krnn",
        "expected": "මං ඔයාට කතා කරන්නං",
        "actual": "mn oyt kth krnn",
        "status": "FAIL",
        "types": "Romanization / Spelling Variants",
        "rationale": (
            "Rationale: All four words are maximally contracted with all vowels removed. "
            "Evidence: 'mn'=mang (I), 'oyt'=oyata (to you), 'kth'=katha (talk), 'krnn'=karanna "
            "(do) — the system cannot parse extreme vowel-stripped Singlish and outputs the raw input."
        ),
    },
    {
        "id": "Neg_0016",
        "length_type": "M",
        "input": "api adha restaurant ekakata gihin kaema kaamu da mchnn?",
        "expected": "අපි අද restaurant එකකට ගිහිං කෑම කාමු ද මචං?",
        "actual": "අපි අද restaurant එකකට ගිහිං කෑම කාමු ද mchnn?",
        "status": "FAIL",
        "types": "Romanization / Spelling Variants",
        "rationale": (
            "Rationale: 'mchnn' is a severely contracted spelling of 'machan' (friend). "
            "Evidence: Removing all vowels from 'machan' → 'mchnn' is a known informal Singlish "
            "contraction — the system fails to recognise it and leaves it as raw Roman text."
        ),
    },

    # ── 9. Isolated English Word Insertions ───────────────────────────────────
    {
        "id": "Neg_0017",
        "length_type": "M",
        "input": "mama ada project eka finish karanna try karanawa",
        "expected": "මම අද project එක finish කරන්න try කරනවා",
        "actual": "මම අද project එක finish කරේනා try කරනවා",
        "status": "FAIL",
        "types": "Isolated English Word Insertions in Singlish",
        "rationale": (
            "Rationale: Single English words 'project', 'finish', and 'try' are inserted into "
            "Singlish. Evidence: Each is a standalone English word — the system incorrectly renders "
            "'karanna' as 'කරේනා' when it follows an English word."
        ),
    },
    {
        "id": "Neg_0018",
        "length_type": "M",
        "input": "oya mage laptop eka charge karadda mama wage kiyala?",
        "expected": "ඔය මගේ laptop එක charge කාරාද්ද මම වගේ කියලා?",
        "actual": "ඔය මගේ laptop එක charge කරාද්ද මම වගේ කියලා?",
        "status": "FAIL",
        "types": "Isolated English Word Insertions in Singlish",
        "rationale": (
            "Rationale: 'laptop' and 'charge' are isolated English insertions. "
            "Evidence: Both are standalone tech-domain English words — the system drops the long ā "
            "in 'karadda', outputting 'කරාද්ද' instead of 'කාරාද්ද'."
        ),
    },

    # ── 10. Multi-Word English Phrases ────────────────────────────────────────
    {
        "id": "Neg_0019",
        "length_type": "M",
        "input": "mama ada feeling totally drained, api katha karamu later ok?",
        "expected": "මම අද feeling totally drained, අපි කතා කරමු later ok?",
        "actual": "මම අද feeling totally drained, අපි කතා කරමු latar ok?",
        "status": "FAIL",
        "types": "Multi-Word English Phrases in Singlish",
        "rationale": (
            "Rationale: 'feeling totally drained' is a consecutive three-word English phrase. "
            "Evidence: Three consecutive English words form an idiomatic phrase — the system "
            "partially distorts 'later' to 'latar' when it follows mixed Singlish."
        ),
    },
    {
        "id": "Neg_0020",
        "length_type": "L",
        "input": (
            "mama hithenne office eke work from home rules change karanna one, ada hama dennek "
            "work from home karanawa wage, eke productivity bohoma drop wela, managers kiyanna "
            "one in person meetings nathnam progress track karanna bari, oyata hari wage wage da "
            "api just get back to normal routine eka? Dan kochara kala giyadha?"
        ),
        "expected": (
            "මම හිතෙන්නේ office එකේ work from home rules change කරන්න ඕනේ, අද හාම දෙනෙක් "
            "work from home කරනවා වගේ, ඒකේ productivity බොහොම drop වෙලා, managers කියන්න "
            "ඕනේ in person meetings නැත්නම් progress track කරන්න බෑ, ඔයාට හරි වගේ ද "
            "අපි just get back to normal routine එක? දැං කොච්චර කාලා ගියාද?"
        ),
        "actual": (
            "මම හිතෙනනේ office eke work from home rules change karanna one, ada hama dennek "
            "work from home karanawa wage, eke productivity bohoma drop wela, managers kiyanna "
            "one in person meetings nathnam progress track karanna bari, oyata hari wage wage da "
            "api just get back to normal routine eka? Dan kochara kala giyadha?"
        ),
        "status": "FAIL",
        "types": "Multi-Word English Phrases in Singlish",
        "rationale": (
            "Rationale: Multiple multi-word English phrases — 'work from home', 'in person meetings', "
            "'progress track', 'just get back to normal routine' — are embedded. "
            "Evidence: Each phrase consists of consecutive English words; the system fails to "
            "transliterate Singlish context around them after the first phrase."
        ),
    },

    # ── 11. English Digital Terms ─────────────────────────────────────────────
    {
        "id": "Neg_0021",
        "length_type": "M",
        "input": "oyage phone eka software update karanna one, battery drain wenawa wadi",
        "expected": "ඔයාගේ phone එක software update කරන්න ඕනේ, battery drain වෙනවා වැඩි",
        "actual": "ඔයාගේ phone eka software update karanna one, battery drain wenawa wadi",
        "status": "FAIL",
        "types": "English Digital Terms in Singlish",
        "rationale": (
            "Rationale: 'software', 'update', 'battery', and 'drain' are English digital terms. "
            "Evidence: These are technical/digital vocabulary words — the system stops transliterating "
            "the Singlish words following the first digital term."
        ),
    },
    {
        "id": "Neg_0022",
        "length_type": "S",
        "input": "server eka down nisa work bari",
        "expected": "server එක down නිසා work බෑ",
        "actual": "server eka down nisa work bari",
        "status": "FAIL",
        "types": "English Digital Terms in Singlish",
        "rationale": (
            "Rationale: 'server' and 'down' are English digital terms meaning a system outage. "
            "Evidence: Both words are IT-domain digital terms — the system fails to transliterate the "
            "Singlish words surrounding them."
        ),
    },

    # ── 12. Platform / App Names ──────────────────────────────────────────────
    {
        "id": "Neg_0023",
        "length_type": "S",
        "input": "Instagram eke reel eka dannada?",
        "expected": "Instagram එකේ reel එක දාන්නද?",
        "actual": "Instagram eke reel eka dannada?",
        "status": "FAIL",
        "types": "Platform/App Names in Singlish",
        "rationale": (
            "Rationale: 'Instagram' is a social-media platform name. "
            "Evidence: 'Instagram' is a proper noun for a well-known app — the system fails to "
            "transliterate the Singlish particles following the platform name."
        ),
    },
    {
        "id": "Neg_0024",
        "length_type": "M",
        "input": "Telegram group eke message ekak danna, Google Meet eka schedule karanna",
        "expected": "Telegram group එකේ message එකක් දාන්න, Google Meet එක schedule කරන්න",
        "actual": "Telegram group eke message ekak danna, Google Meet eka schedule karanna",
        "status": "FAIL",
        "types": "Platform/App Names in Singlish",
        "rationale": (
            "Rationale: 'Telegram' and 'Google Meet' are platform/app names. "
            "Evidence: Both are proper nouns for digital communication platforms — their presence "
            "causes the system to leave all surrounding Singlish particles untransliterated."
        ),
    },

    # ── 13. English Abbreviations / Acronyms ──────────────────────────────────
    {
        "id": "Neg_0025",
        "length_type": "S",
        "input": "DOB eka correct da?",
        "expected": "DOB එක correct ද?",
        "actual": "DOB eka correct da?",
        "status": "FAIL",
        "types": "English Abbreviations/Acronyms in Singlish",
        "rationale": (
            "Rationale: 'DOB' is the acronym for Date of Birth. "
            "Evidence: 'DOB' is an all-caps abbreviation — the system leaves both the acronym and the "
            "surrounding Singlish words ('eka', 'da') untransliterated."
        ),
    },
    {
        "id": "Neg_0026",
        "length_type": "M",
        "input": "mama POC ekek karanna one, COD payments support karanawada me site eke?",
        "expected": "මම POC එකක් කරන්න ඕනේ, COD payments support කරනවාද මේ site එකේ?",
        "actual": "මම POC ekek karanna one, COD payments support karanawada me site eke?",
        "status": "FAIL",
        "types": "English Abbreviations/Acronyms in Singlish",
        "rationale": (
            "Rationale: 'POC' (Proof of Concept) and 'COD' (Cash on Delivery) are abbreviations. "
            "Evidence: Both are uppercase abbreviations embedded in Singlish — the system translates "
            "the initial Sinhala word but fails on everything after the first acronym."
        ),
    },

    # ── 14. English Clipped Forms ─────────────────────────────────────────────
    {
        "id": "Neg_0027",
        "length_type": "S",
        "input": "heta uni eke exam ekak",
        "expected": "හෙට uni එකේ exam එකක්",
        "actual": "හෙට uni eke exam ekak",
        "status": "FAIL",
        "types": "English Clipped Forms in Singlish",
        "rationale": (
            "Rationale: 'uni' is a clipped form of 'university'. "
            "Evidence: 'uni' is a shortened English word used informally — the system keeps the "
            "Singlish particles 'eke' and 'ekak' in Roman script instead of transliterating them."
        ),
    },
    {
        "id": "Neg_0028",
        "length_type": "M",
        "input": "gym eke sub karala hitiya baduwa ada promo eke tiyenawa",
        "expected": "gym එකේ sub කරලා හිතිය බඩු අද promo එකේ තියෙනවා",
        "actual": "gym eke sub karala hitiya baduwa ada promo eke tiyenawa",
        "status": "FAIL",
        "types": "English Clipped Forms in Singlish",
        "rationale": (
            "Rationale: 'gym' is clipped from 'gymnasium' and 'promo' from 'promotion'. "
            "Evidence: Both are shortened English words embedded in Singlish — the system fails to "
            "transliterate any of the Singlish words in the sentence."
        ),
    },

    # ── 15. Place Names ───────────────────────────────────────────────────────
    {
        "id": "Neg_0029",
        "length_type": "S",
        "input": "Colombo 07 kiyannet koheda?",
        "expected": "Colombo 07 කියන්නේ කොහෙද?",
        "actual": "Colombo 07 kiyannet koheda?",
        "status": "FAIL",
        "types": "Place Names Embedded in Singlish",
        "rationale": (
            "Rationale: 'Colombo 07' is a Sri Lankan place name with a number. "
            "Evidence: 'Colombo 07' is a proper geographical noun — the system fails to transliterate "
            "the question words that follow the place name and number."
        ),
    },
    {
        "id": "Neg_0030",
        "length_type": "M",
        "input": "Kandy eken Nuwara Eliya walata yanawa, mehema train eken",
        "expected": "Kandy එකෙං Nuwara Eliya වලට යනවා, මෙහෙම train එකෙං",
        "actual": "Kandy ekeng Nuwara Eliya walata yanawa, mehema train ekeng",
        "status": "FAIL",
        "types": "Place Names Embedded in Singlish",
        "rationale": (
            "Rationale: 'Kandy' and 'Nuwara Eliya' are Sri Lankan city names. "
            "Evidence: Both are proper geographical nouns — the system keeps the Singlish words "
            "between the place names in Roman script, failing to transliterate them."
        ),
    },

    # ── 16. Person Names ──────────────────────────────────────────────────────
    {
        "id": "Neg_0031",
        "length_type": "S",
        "input": "Nimali gihin da?",
        "expected": "Nimali ගිහිංද?",
        "actual": "Nimali gihin da?",
        "status": "FAIL",
        "types": "Person Names Embedded in Singlish",
        "rationale": (
            "Rationale: 'Nimali' is a personal name used as the subject. "
            "Evidence: 'Nimali' is a proper noun (female personal name) — the presence of the name "
            "at the start causes the system to leave the subsequent Singlish words untransliterated."
        ),
    },
    {
        "id": "Neg_0032",
        "length_type": "M",
        "input": "Dinesh saha Priyanka dennama project eke work karanawa, supiriyatama",
        "expected": "Dinesh සහ Priyanka දෙන්නම project එකේ work කරනවා, සුපිරියටම",
        "actual": "Dinesh sahaa Priyanka dennama project eke work karanawa, supiriyatama",
        "status": "FAIL",
        "types": "Person Names Embedded in Singlish",
        "rationale": (
            "Rationale: 'Dinesh' and 'Priyanka' are personal names. "
            "Evidence: Both are proper nouns for individuals — the system incorrectly maps 'saha' to "
            "'sahaa' with a doubled vowel and fails on the remaining Singlish particles."
        ),
    },

    # ── 17. Numbers and Numeric Suffixes ──────────────────────────────────────
    {
        "id": "Neg_0033",
        "length_type": "M",
        "input": "mata 2nd attempt eke pass wennam kiyala hithuwa",
        "expected": "මට 2nd attempt එකේ pass වෙන්නම් කියලා හිතුව",
        "actual": "මට 2nd attempt eke pass wennam kiyala hithuwa",
        "status": "FAIL",
        "types": "Inputs with Numbers and Numeric Suffixes",
        "rationale": (
            "Rationale: '2nd' contains the numeric ordinal suffix 'nd'. "
            "Evidence: '2nd' combines numeral '2' with suffix 'nd' — the system transliterates only "
            "'මට' and then fails when it encounters the numeric-suffix token."
        ),
    },
    {
        "id": "Neg_0034",
        "length_type": "S",
        "input": "3rd floor eke office eka",
        "expected": "3rd floor එකේ office එක",
        "actual": "3rd floor eke office eka",
        "status": "FAIL",
        "types": "Inputs with Numbers and Numeric Suffixes",
        "rationale": (
            "Rationale: '3rd' is a numeric ordinal with suffix 'rd'. "
            "Evidence: '3rd' combines the numeral '3' with the ordinal suffix 'rd' representing floor "
            "level — the system fails to transliterate the Singlish particles after this token."
        ),
    },

    # ── 18. Currency ──────────────────────────────────────────────────────────
    {
        "id": "Neg_0035",
        "length_type": "S",
        "input": "USD 50 kochcharada rupiyel walin?",
        "expected": "USD 50 කොච්චරද රුපියෙල් වලිං?",
        "actual": "USD 50 kochchara da rupiyel walin?",
        "status": "FAIL",
        "types": "Inputs with Currency",
        "rationale": (
            "Rationale: 'USD' is a currency code for US Dollar. "
            "Evidence: 'USD' is an international currency abbreviation — the system fails to "
            "transliterate the Singlish words after the currency code and number."
        ),
    },
    {
        "id": "Neg_0036",
        "length_type": "M",
        "input": "eka GBP 200 witarada, danissima yamu wage maha gathiyak wage neh",
        "expected": "ඒක GBP 200 විතරද, දැනිස්සිම යමු වගේ මහ ගාතියක් වගේ නේ",
        "actual": "eka GBP 200 witarada, danissima yamu wage maha gathiyak wage neh",
        "status": "FAIL",
        "types": "Inputs with Currency",
        "rationale": (
            "Rationale: 'GBP' is the currency abbreviation for British Pound Sterling. "
            "Evidence: 'GBP' is an uppercase currency code — the system fails to transliterate the "
            "surrounding Singlish words due to the mid-sentence currency code."
        ),
    },

    # ── 19. Time Formats ──────────────────────────────────────────────────────
    {
        "id": "Neg_0037",
        "length_type": "S",
        "input": "9:00AM api yanawa bus eka",
        "expected": "9:00AM අපි යනවා bus එක",
        "actual": "9:00AM api yanawa bus eka",
        "status": "FAIL",
        "types": "Inputs with Time Formats",
        "rationale": (
            "Rationale: '9:00AM' is a 12-hour clock time format with AM suffix. "
            "Evidence: '9:00AM' uses a colon separator with uppercase AM — the system fails to "
            "transliterate the Singlish words that follow the time token."
        ),
    },
    {
        "id": "Neg_0038",
        "length_type": "M",
        "input": "meeting eka 2:30pm walata cancel kala, 4:00pm walata reschedule karala tiyenawa",
        "expected": "meeting එක 2:30pm වලට cancel කළා, 4:00pm වලට reschedule කරලා තියෙනවා",
        "actual": "meeting eka 2:30pm walata cancel kala, 4:00pm walata reschedule karala tiyenawa",
        "status": "FAIL",
        "types": "Inputs with Time Formats",
        "rationale": (
            "Rationale: '2:30pm' and '4:00pm' are two time formats embedded in one sentence. "
            "Evidence: Both use lowercase pm — the system is unable to handle multiple time tokens "
            "and fails to transliterate any of the surrounding Singlish words."
        ),
    },

    # ── 20. Dates ─────────────────────────────────────────────────────────────
    {
        "id": "Neg_0039",
        "length_type": "S",
        "input": "March 05 birthday eka",
        "expected": "March 05 birthday එක",
        "actual": "March 05 birthday eka",
        "status": "FAIL",
        "types": "Inputs with Dates",
        "rationale": (
            "Rationale: 'March 05' is a partial date (month + day). "
            "Evidence: 'March 05' combines an English month name with a day number — the system "
            "leaves 'eka' in Roman script instead of transliterating it to 'එක'."
        ),
    },
    {
        "id": "Neg_0040",
        "length_type": "M",
        "input": "2025/12/25 Christmas da, api koheda yanawa oyala?",
        "expected": "2025/12/25 Christmas ද, අපි කොහෙද යනවා ඔයාලා?",
        "actual": "2025/12/25 Christmas da, api koheda yanawa oyala?",
        "status": "FAIL",
        "types": "Inputs with Dates",
        "rationale": (
            "Rationale: '2025/12/25' is a full date in YYYY/MM/DD format with forward-slash separators. "
            "Evidence: The date format combined with the holiday name 'Christmas' causes the system "
            "to fail on all subsequent Singlish question words."
        ),
    },

    # ── 21. Units of Measurement ──────────────────────────────────────────────
    {
        "id": "Neg_0041",
        "length_type": "M",
        "input": "500ml bottle ekak ganna, mama kaema metti karana eka widihata hadannam",
        "expected": "500ml bottle එකක් ගන්න, මම කෑම මෙට්ටි කරන එක විදිහට හදන්නම්",
        "actual": "500ml bottle ekak ganna, mama kaema metti karana eka widihata hadannam",
        "status": "FAIL",
        "types": "Inputs with Unit of Measurements",
        "rationale": (
            "Rationale: '500ml' is a volume measurement unit. "
            "Evidence: '500ml' combines numeral '500' with unit abbreviation 'ml' (millilitre) — "
            "the system fails to transliterate the Singlish words that follow the unit token."
        ),
    },
    {
        "id": "Neg_0042",
        "length_type": "S",
        "input": "2kg sugar gedara genenna",
        "expected": "2kg sugar ගෙදර ගෙනෙන්න",
        "actual": "2kg sugar gedara genenna",
        "status": "FAIL",
        "types": "Inputs with Unit of Measurements",
        "rationale": (
            "Rationale: '2kg' is a mass measurement unit. "
            "Evidence: '2kg' combines numeral '2' with unit abbreviation 'kg' (kilogram) — "
            "the system fails to transliterate 'gedara genenna' into Sinhala."
        ),
    },

    # ── 22. Slang and Casual Phrasing ─────────────────────────────────────────
    {
        "id": "Neg_0043",
        "length_type": "S",
        "input": "mara elakiri work bro!",
        "expected": "මාර එළකිරි work bro!",
        "actual": "mara elakiri work bro!",
        "status": "FAIL",
        "types": "Inputs with Slang and Casual Phrasing",
        "rationale": (
            "Rationale: 'mara elakiri' is a Singlish slang phrase meaning 'extremely awesome'. "
            "Evidence: 'mara' is a Singlish intensifier and 'elakiri' is a slang term for "
            "'excellent/cool' — the system fails to transliterate both slang words."
        ),
    },
    {
        "id": "Neg_0044",
        "length_type": "M",
        "input": "uba aiye, me project eka daana palayan, hama thissema set neh",
        "expected": "උඹ අයියේ, මේ project එක දාන පලයං, හාම තිස්සෙම set නේ",
        "actual": "uba aiye, me project eka daana palayan, hama thissema set neh",
        "status": "FAIL",
        "types": "Inputs with Slang and Casual Phrasing",
        "rationale": (
            "Rationale: 'uba', 'palayan', and 'set neh' are casual/slang expressions. "
            "Evidence: 'uba' is a very informal second-person pronoun, 'palayan' means 'get lost' "
            "(rude dismissal), and 'set neh' means 'it's not working' in Singlish slang."
        ),
    },

    # ── 23. Online Identifiers ────────────────────────────────────────────────
    {
        "id": "Neg_0045",
        "length_type": "M",
        "input": "mata me link eka ewanna: www.example.lk, mama check karanna",
        "expected": "මට මේ link එක එවන්න: www.example.lk, මම check කරන්න",
        "actual": "mata me link eka ewanna: www.example.lk, mama check karanna",
        "status": "FAIL",
        "types": "Online Identifiers in Singlish",
        "rationale": (
            "Rationale: 'www.example.lk' is a URL (online identifier). "
            "Evidence: The web address uses 'www.' prefix — the system fails entirely when a URL is "
            "present, leaving all Singlish words in the sentence untransliterated."
        ),
    },
    {
        "id": "Neg_0046",
        "length_type": "M",
        "input": "oya @Kasun ayyata message karawa da, eyata kiyanna urgent kiyala",
        "expected": "ඔය @Kasun අය්‍යාට message කෑරාව ද, එයාට කියන්න urgent කියලා",
        "actual": "oya @Kasun ayyata message karawa da, eyata kiyanna urgent kiyala",
        "status": "FAIL",
        "types": "Online Identifiers in Singlish",
        "rationale": (
            "Rationale: '@Kasun' is a social-media mention identifier. "
            "Evidence: '@Kasun' uses the '@' symbol as a social mention prefix — its presence "
            "causes the system to leave all surrounding Singlish text untransliterated."
        ),
    },

    # ── 24. Inputs Containing Emojis ──────────────────────────────────────────
    {
        "id": "Neg_0047",
        "length_type": "S",
        "input": "bohoma pin \U0001f64f",
        "expected": "බොහොම පිං \U0001f64f",
        "actual": "bohoma pin \U0001f64f",
        "status": "FAIL",
        "types": "Inputs Containing Emojis",
        "rationale": (
            "Rationale: The 🙏 emoji follows Singlish text expressing gratitude. "
            "Evidence: The 🙏 emoji appears at the end of the expression 'bohoma pin' (very meritorious) "
            "— the system fails to transliterate the Singlish words when an emoji is present."
        ),
    },
    {
        "id": "Neg_0048",
        "length_type": "M",
        "input": "machan, meka balanna \U0001f62d api hadapu wage neh oyage idea eka",
        "expected": "මචං, මෙක බලන්න \U0001f62d අපි හදාපු වගේ නේ ඔයාගේ idea එක",
        "actual": "machan, meka balanna \U0001f62d api hadapu wage neh oyage idea eka",
        "status": "FAIL",
        "types": "Inputs Containing Emojis",
        "rationale": (
            "Rationale: The 😭 emoji is embedded mid-sentence between two Singlish clauses. "
            "Evidence: The crying emoji divides the sentence — its mid-sentence position "
            "disrupts the system's ability to transliterate any part of the input."
        ),
    },

    # ── 25–26. Extra cases (any type) ─────────────────────────────────────────
    {
        "id": "Neg_0049",
        "length_type": "M",
        "input": "oya hadapu project eka koheda submit karanne kiyala dannawada?",
        "expected": "ඔය හදාපු project එක කොහෙද submit කරන්නේ කියලා දන්නවාද?",
        "actual": "oya hadapu project eka koheda submit karanne kiyala dannawada?",
        "status": "FAIL",
        "types": "Question forms",
        "rationale": (
            "Rationale: A question about where to submit a project. "
            "Evidence: 'koheda' is the question word for 'where' and 'dannawada' forms the "
            "interrogative suffix — the English word 'submit' causes the system to stop transliterating."
        ),
    },
    {
        "id": "Neg_0050",
        "length_type": "M",
        "input": "poddak balanna, mama enna giyamath danna, okay da?",
        "expected": "පොඩ්ඩක් බලන්න, මම එන්න ගියාමත් දාන්න, okay ද?",
        "actual": "poddak balanna, mama enna giyamath danna, okay da?",
        "status": "FAIL",
        "types": "Command forms",
        "rationale": (
            "Rationale: Contains two imperative commands followed by a confirmation question. "
            "Evidence: 'balanna' and 'danna' are both imperative Singlish verbs — the English "
            "word 'okay' causes the system to fail on transliterating the full command sequence."
        ),
    },
]
