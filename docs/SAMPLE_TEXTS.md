# 📝 Sample Texts for Testing

Используйте эти тексты для демонстрации работы Text Summarizer.

---

## 1. Technology Article (Medium Length)

**Topic:** Artificial Intelligence

```
Artificial intelligence (AI) is revolutionizing the way we live and work. From virtual assistants like Siri and Alexa to self-driving cars and advanced medical diagnostics, AI is becoming increasingly integrated into our daily lives. Machine learning, a subset of AI, allows computers to learn from data without being explicitly programmed. Deep learning, which uses neural networks with multiple layers, has enabled breakthroughs in image recognition, natural language processing, and game playing. However, the rise of AI also raises important ethical questions about privacy, job displacement, and the potential for bias in automated decision-making systems. As we continue to develop more sophisticated AI systems, it's crucial that we address these concerns and ensure that AI is developed and deployed responsibly for the benefit of all humanity.
```

**Expected Summary:** ~3-4 sentences about AI revolution, applications, and ethical concerns.

---

## 2. Historical Event (Long)

**Topic:** Moon Landing

```
On July 20, 1969, Apollo 11 astronauts Neil Armstrong and Buzz Aldrin became the first humans to land on the Moon, while Michael Collins orbited above in the command module. The historic mission was the culmination of years of work by NASA and thousands of engineers, scientists, and support staff. President John F. Kennedy had set the ambitious goal in 1961 of landing a man on the Moon and returning him safely to Earth before the end of the decade. The space race with the Soviet Union provided additional motivation for this unprecedented achievement. Armstrong's famous words, "That's one small step for man, one giant leap for mankind," were broadcast to millions of people watching on television around the world. The mission collected lunar samples, conducted experiments, and planted the American flag on the lunar surface. The success of Apollo 11 demonstrated American technological prowess and marked a pivotal moment in human history. The Moon landing inspired generations of scientists, engineers, and dreamers, and remains one of humanity's greatest accomplishments in space exploration.
```

**Expected Summary:** ~4-5 sentences about Apollo 11 mission, achievement, and impact.

---

## 3. Business News (Short)

**Topic:** Tech Company Announcement

```
Apple Inc. announced its latest iPhone model today, featuring advanced camera capabilities, improved battery life, and a faster processor. The new device will be available in four colors and multiple storage configurations. Pre-orders begin next Friday, with the official launch scheduled for the following week. The company's CEO emphasized the phone's environmental features, including recycled materials and energy-efficient components. Industry analysts predict strong sales despite the premium pricing.
```

**Expected Summary:** ~2-3 sentences about new iPhone announcement and features.

---

## 4. Scientific Discovery (Technical)

**Topic:** CRISPR Gene Editing

```
CRISPR-Cas9 is a revolutionary gene-editing technology that allows scientists to precisely modify DNA sequences in living organisms. The system uses a guide RNA to direct the Cas9 enzyme to a specific location in the genome, where it makes a cut. The cell's natural repair mechanisms then fix the break, either by disrupting the gene or by incorporating a new sequence provided by researchers. This technology has enormous potential for treating genetic diseases, developing new crops, and advancing our understanding of biology. Recent applications include correcting mutations that cause sickle cell anemia and muscular dystrophy. However, the technology also raises ethical concerns, particularly regarding germline editing that could affect future generations. Scientists and ethicists continue to debate the appropriate uses and limitations of CRISPR technology as it becomes more accessible and powerful.
```

**Expected Summary:** ~3-4 sentences about CRISPR technology, applications, and ethical concerns.

---

## 5. Simple Story (Very Short)

**Topic:** Daily Life

```
Sarah woke up early and decided to go for a morning run. The weather was perfect with clear skies and a gentle breeze. She ran through the park, enjoying the peaceful atmosphere. After her run, she stopped at a café for coffee and breakfast. It was a great start to her day.
```

**Expected Summary:** ~1-2 sentences about morning routine.

---

## 6. Movie Review (Medium)

**Topic:** Film Criticism

```
Christopher Nolan's "Inception" is a mind-bending thriller that explores the nature of reality and dreams. The film follows Dom Cobb, a skilled thief who steals secrets from people's subconscious while they dream. When offered a chance to have his criminal record erased, Cobb accepts a dangerous mission: instead of stealing an idea, he must plant one deep within a target's subconscious. The concept of "inception" is achieved by creating dreams within dreams, each layer becoming increasingly unstable. Leonardo DiCaprio delivers a powerful performance as the tormented protagonist, while the supporting cast, including Ellen Page, Tom Hardy, and Marion Cotillard, bring depth to their complex characters. Hans Zimmer's haunting score perfectly complements the film's intense atmosphere. Nolan's masterful direction combines stunning visual effects with an intricate narrative that keeps viewers engaged and guessing until the ambiguous final scene. Despite its complexity, "Inception" became both a critical and commercial success, spawning countless discussions about its themes and ending.
```

**Expected Summary:** ~3-4 sentences about Inception plot, cast, and reception.

---

## 7. Health & Wellness (Educational)

**Topic:** Exercise Benefits

```
Regular physical exercise provides numerous benefits for both physical and mental health. Cardiovascular exercises like running, swimming, and cycling strengthen the heart and improve circulation. Strength training builds muscle mass, increases bone density, and boosts metabolism. Exercise also releases endorphins, which are natural mood elevators that help reduce stress and anxiety. Studies have shown that regular physical activity can lower the risk of chronic diseases such as diabetes, heart disease, and certain cancers. Additionally, exercise improves sleep quality, cognitive function, and overall quality of life. Experts recommend at least 150 minutes of moderate aerobic activity or 75 minutes of vigorous activity per week, combined with strength training exercises twice a week. It's important to choose activities you enjoy and to start gradually, especially if you're new to exercise. Consulting with a healthcare provider before beginning a new exercise program is always advisable.
```

**Expected Summary:** ~3-4 sentences about exercise benefits and recommendations.

---

## 8. Travel Guide (Descriptive)

**Topic:** Paris Tourism

```
Paris, the capital of France, is one of the world's most visited cities, attracting millions of tourists each year. The city is famous for its iconic landmarks, including the Eiffel Tower, Notre-Dame Cathedral, and the Arc de Triomphe. Art enthusiasts flock to world-class museums like the Louvre, which houses the Mona Lisa, and the Musée d'Orsay, known for its impressionist masterpieces. Parisian cuisine is renowned globally, offering everything from elegant Michelin-starred restaurants to charming neighborhood bistros and bustling street markets. The city's distinct neighborhoods, or arrondissements, each have their own character: Montmartre with its bohemian atmosphere and Sacré-Cœur basilica, the Latin Quarter with its student life and historic streets, and Le Marais with its trendy boutiques and medieval architecture. Strolling along the Seine River, shopping on the Champs-Élysées, or simply enjoying coffee at a sidewalk café are quintessential Parisian experiences. The city's efficient metro system makes it easy to navigate, though walking through its picturesque streets is often the best way to discover hidden gems.
```

**Expected Summary:** ~3-4 sentences about Paris attractions and experiences.

---

## Testing Tips

### For Quick Testing:
Use texts #5 (Simple Story) or #3 (Business News) for fast results.

### For Impressive Demos:
Use texts #2 (Moon Landing) or #6 (Movie Review) - они показывают способность обрабатывать длинные тексты.

### For Technical Demos:
Use text #4 (CRISPR) to show handling of scientific content.

### Command Line Testing:

```bash
# Test with text #3 (Business News)
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Apple Inc. announced its latest iPhone model today, featuring advanced camera capabilities, improved battery life, and a faster processor. The new device will be available in four colors and multiple storage configurations. Pre-orders begin next Friday, with the official launch scheduled for the following week. The company'\''s CEO emphasized the phone'\''s environmental features, including recycled materials and energy-efficient components. Industry analysts predict strong sales despite the premium pricing."
  }'
```

---

## Troubleshooting

### If summaries are too short:
- Try longer input texts (#2, #6, #8)
- Adjust model parameters (if using local model)

### If summaries are too long:
- Use shorter input texts (#3, #5)
- Check model configuration

### If summaries are irrelevant:
- Verify API keys are correct
- Check worker logs: `make logs-worker`
- Test different model backends

---

**Pro Tip:** Для создания скриншотов, используйте текст #2 (Moon Landing) - он дает впечатляющие результаты!
