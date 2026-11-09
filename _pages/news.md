---
layout: page
title: "News"
permalink: /news/
description: "Dated updates from Moonseong (Bronson) Jeong: preprints, papers, talks, and teaching."
---

{% assign news_items = site.data.news | sort: "key" | reverse %}
<div class="news">
{% for item in news_items %}
  <article class="news__item">
    <time datetime="{{ item.date }}">{{ item.date | date: "%B %Y" }}</time>
    <p>{{ item.text | markdownify | remove: "<p>" | remove: "</p>" }}</p>
  </article>
{% endfor %}
</div>
