import {defineConfig} from 'vitepress';
import {glob} from 'glob';
import * as path from 'path';

// https://vitepress.dev/reference/site-config
export default defineConfig({
    lang: 'fr-CH',
    title: "MSIG-24",
    description: "Stage professionnel pour obtenir le passeport vers la HEG",
    head: [
        ['link', {rel: "icon", href: "logo.svg"}],
    ],
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        logo: 'logo.svg',
        nav: [
            {text: 'Accueil', link: '/'},
            {text: 'Thématiques', link: '/thematiques/'},
            {text: 'Supports', link: '/supports/'},
            {text: 'Activités', link: '/activites/'}
        ],
        outline: {label: "Sur cette page"},
        docFooter: {prev: "Précédent", next: "Suivant"},
        returnToTopLabel:"Retourner au début",

        sidebar: [
            {
                text: 'Thématiques',
                collapsed: false,
                items: glob.sync('thematiques/**/*.md', {ignore: '*/**README.md', posix: true})
                    .map(file => ({text: `${path.basename(file).replace(".md", "")}`, link: `/${file}`})).reverse()
            },
            {
                text: 'Supports',
                collapsed: true,
                items: glob.sync('supports/**/*.md', {ignore: '*/**README.md', posix: true})
                    .map(file => ({text: `${path.basename(file).replace(".md", "")}`, link: `/${file}`})).reverse()
            },
            {
                text: 'Activités',
                collapsed: true,
                items: glob.sync('activites/**/README.md', {ignore: 'activites/README.md', posix: true})
                    .map(file => ({
                        text: `${file.split("/")[1]}`,
                        link: `/${file.replace("README", "index")}`
                    })).reverse()
            },

        ],
        search: {
            provider: 'local',
            options: {
                translations: {
                    button: {buttonText: "Rechercher", buttonAriaLabel: "Rechercher"},
                    modal: {
                        displayDetails: "Voir les détails",
                        footer: {selectText: "Valider",closeText:"Fermer",navigateText:"Pour naviguer"}
                    },
                }
            }
        },

        socialLinks: [
            {icon: 'github', link: 'https://github.com/jonathanMelly/msig24'}
        ]
    },
    base: "/msig24/",//for gh pages
    rewrites: {
        'README.md': 'index.md',
        '(.*)/README.md': '(.*)/index.md'
    },
    lastUpdated: true,
})
