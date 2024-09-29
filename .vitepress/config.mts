import {glob} from 'glob';
import * as path from 'path';
import fg from 'fast-glob'
import fs from 'node:fs/promises'
import { dirname } from 'node:path'
import { withMermaid } from "vitepress-plugin-mermaid";
import taskLists from 'markdown-it-task-lists'
import { full as emoji } from 'markdown-it-emoji'

// https://vitepress.dev/reference/site-config
export default withMermaid({
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
        lastUpdated: {
            text: 'Dernière mise à jour',
            formatOptions: {
                dateStyle: 'full',
                timeStyle: 'short'
            }
        },
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
    markdown: {
        math: true,
        config: (md) => {
            md
                .use(taskLists)
                .use(emoji)
        }
    },
    async buildEnd({ srcDir: src, outDir: dest }) {
        //Copy other assets...
        const files = await fg(['**/*', '!**/*.md'], { cwd: src, absolute: true })
        await Promise.all(
            files.map(async (file) => {
                const destFile = file.replace(src, dest)
                await fs.mkdir(dirname(destFile), { recursive: true })
                await fs.copyFile(file, destFile)
            })
        )
    },
    mermaid: {
        // refer https://mermaid.js.org/config/setup/modules/mermaidAPI.html#mermaidapi-configuration-defaults for options
    },
    /*ignoreDeadLinks: [
        /\.docx$/,
    ]*/
});



