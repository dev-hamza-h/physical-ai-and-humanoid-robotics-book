// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI Humanoid Robotics Book',
  tagline: 'An open-source book on building physical AI humanoid robots.',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // Vercel site URL
  url: 'https://physical-ai-and-humanoid-robotics-b-sigma.vercel.app',
  baseUrl: '/',

  // GitHub repo info
  organizationName: 'dev-hamza-h',
  projectName: 'physical-ai-and-humanoid-robotics-book',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/dev-hamza-h/physical-ai-and-humanoid-robotics-book-06/tree/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig: ({
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI Humanoid Robotics',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Book',
        },
        {
          href: 'https://github.com/dev-hamza-h/physical-ai-and-humanoid-robotics-book-06',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/dev-hamza-h/physical-ai-and-humanoid-robotics-book-06',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI Humanoid Robotics — Authored by Hamza Hassan`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  }),
};

export default config;
