---
layout: archive
title: "News"
permalink: /news/
description: "Research news and updates from Moonseong (Bronson) Jeong: preprints, publications, talks, and teaching."
author_profile: false
---

{% assign news_items = site.data.news | sort: "date" | reverse %}
<div class="news-list news-list--page">
{% for item in news_items %}
  <article class="news-item">
    <time datetime="{{ item.date }}">{{ item.date | date: "%B %Y" }}</time>
    <p>{{ item.text | markdownify | remove: "<p>" | remove: "</p>" }}</p>
  </article>
{% endfor %}
</div>
